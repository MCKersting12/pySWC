import unittest
import pyswc

test_file = pyswc.Swc('test_file.swc')


class TestSwc(unittest.TestCase):

    def test_isolate_type(self):

        isolated = pyswc.isolate_type(test_file, [2])

        self.assertEqual(isolated.num_nodes, 3)

    def test_surface_area_calculation(self):

        isolated = pyswc.isolate_type(test_file, [4])

        target = 114.06

        self.assertEqual(round(isolated.surface_area, 2), target)


if __name__ == "__main__":
    unittest.main()
