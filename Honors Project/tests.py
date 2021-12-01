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




if __name__ == "__main__":
    unittest.main()