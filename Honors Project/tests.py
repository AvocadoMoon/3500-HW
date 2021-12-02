import convexhull as ch
import unittest

class TestLine(unittest.TestCase):

    def setUp(self):
        a = (1, 1)
        b = (2, 2)
        self.line = ch.Line(a, b)

    def test_Slope(self):
        self.assertEqual(self.line.m, 1)
    
    def test_Yintercept(self):
        self.assertEqual(self.line.yInt, 0)
    
    def test_pointSlope(self):
        y = self.line.pointSlope(3)
        self.assertEqual(y, 3)
    
    def test_pointSlopeY(self):
        x = self.line.pointSlopeY(3)
        self.assertEqual(x, 3)

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
    

    def test_inBetween(self):
        leftSide = ch.Line((1, 1), (2, 4))
        self.assertEqual(leftSide.m, 3)
        self.assertEqual(leftSide.yInt, -2)

        rightSide = ch.Line((3, 2), (4, 5))
        self.assertEqual(rightSide.m, 3)
        self.assertEqual(rightSide.yInt, -7)

        f = ch.inBetween(leftSide, rightSide, (2, 3))
        self.assertTrue(f)

        f= ch.inBetween(leftSide, rightSide, (0, 0))
        self.assertTrue(not(f))




if __name__ == "__main__":
    unittest.main()