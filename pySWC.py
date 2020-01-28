# -*- coding: utf-8 -*-
"""
pyswc is designed for the manipulation of swc files
"""
import numpy as np

class Swc:
    
    def __init__(self, filename):
        
        self.data = np.genfromtxt(filename)
        self.num_nodes = self.data.shape[0]
        self.surface_area =  self.find_surface_area()
        
    def save_file(self, filename):
        
        np.savetxt(filename, self.data, fmt='%i %i %4.12f %4.12f %4.12f %4.5f %i')  

    def relabel(self, old, new):
        
        for i in range(0,self.num_nodes):
            if self.data[i, 1] == old:
                self.data[i, 1] = new

    def scale(self, scale_factor, scale_radii=True):
        
        for i in range(0,self.num_nodes):
            
            self.data[i,2] = self.data[i,2] * scale_factor
            self.data[i,3] = self.data[i,3] * scale_factor
            self.data[i,4] = self.data[i,4] * scale_factor
            if scale_radii == True:
                self.data[i,5] = self.data[i,5] * scale_factor
            
        self.surface_area =  self.find_surface_area()
        
    def translate(self, x_translation, y_translation, z_translation):
        
        for i in range(0,self.num_nodes):
            
            self.data[i,2] = self.data[i,2] + x_translation
            self.data[i,3] = self.data[i,3] + y_translation
            self.data[i,4] = self.data[i,4] + z_translation
            
    def find_surface_area(self):
        
        total_area = 0.0
        for i in range(0, self.num_nodes-1):
            x_dist = np.abs(self.data[i,2] - self.data[i+1, 2])
            y_dist = np.abs(self.data[i,3] - self.data[i+1, 3])
            z_dist = np.abs(self.data[i,4] - self.data[i+1, 4])
            total_dist = np.sqrt(x_dist**2 + y_dist**2 + z_dist**2)
            section_area = (np.pi*(self.data[i,5]+self.data[i+1,5]))*(np.sqrt(total_dist**2+(self.data[i+1,5]-self.data[i,5])**2))
            total_area += section_area
        
        return(total_area)

    def adjust_surface_area(self, goal_surface_area, error_rate=0.001):
        
        while((np.abs(self.surface_area - goal_surface_area)/goal_surface_area) > error_rate ):
            new_swc = self.data
            scaling_factor = goal_surface_area / self.surface_area
            for i in range(0, self.num_nodes):
                new_swc[i, 5] = scaling_factor * self.data[i, 5]
            self.data = new_swc
            self.surface_area = self.find_surface_area()
    