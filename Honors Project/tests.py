import convexhull as ch
import unittest

class TestHull(unittest.TestCase):

    def test_twoTriangles(self):
        # points = [(186, 81), (250, 143), (130, 206), (532, 93), (478, 144), (573, 200)]
        # expected_points = [(186,81), (130, 206), (532, 93), (573, 200)]
        # ch.clockwiseSort(expected_points)
        # hull, f = ch.computeHull(points)
        # self.assertEqual(expected_points, hull)

        points = [(117, 212), (170, 76), (239, 161), (590, 102), (657, 73), (693, 174)]
        expected_points = [(117, 212), (170,76), (657, 73), (693, 174)]
        ch.clockwiseSort(expected_points)
        hull, f = ch.computeHull(points)
        self.assertEqual(expected_points, hull)

class TestHelperFunctions(unittest.TestCase):

    # def test_Tangent(self):
    #     ch.tangent()
    

    def test_rightMostIndex(self):
        pass




if __name__ == "__main__":
    unittest.main()