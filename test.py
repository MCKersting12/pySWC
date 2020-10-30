import unittest
import pyswc


class TestSwc(unittest.TestCase):

    def test_isolate_type(self):

        test_file = pyswc.Swc('test_file.swc')

        isolated = pyswc.isolate_type(test_file, [2])

        self.assertEqual(isolated.num_nodes, 3)

    def test_surface_area_calculation(self):

        test_file = pyswc.Swc('test_file.swc')

        isolated = pyswc.isolate_type(test_file, [4])

        target = 114.06

        self.assertEqual(round(isolated.surface_area, 2), target)

    def test_scale_function(self):

        test_file = pyswc.Swc('test_file.swc')

        test_file.scale(0.1)

        self.assertEqual(round(test_file.data[0][2], 2), -15.39)


if __name__ == "__main__":
    unittest.main()
