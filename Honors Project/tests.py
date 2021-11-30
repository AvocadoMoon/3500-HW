import convexhull as ch
import unittest

class TestTangent(unittest.TestCase):

    def test_Slope(self):
        a = (1, 1)
        b = (2, 2)
        m = ch.slope(a, b)
        self.assertEqual(m, 1)
    
    def test_Yintercept(self):
        a = (1, 1)
        b = (2, 2)
        m = 1
        y = ch.yIntercept(a, m, b)
        self.assertEqual(y, 0)
    
    def test_YForm(self):
        a = (1, 1)
        b = (2, 2)
        m = 1
        x = ch.yInterceptForm(m, 3, 0)
        self.assertEqual(x, 3)




if __name__ == "__main__":
    unittest.main()