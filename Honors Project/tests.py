import convexhull as ch
import unittest
import random
from tkinter import *
import time

class TestHull(unittest.TestCase):

    def time(self, string):
        print(string + "%f")

    def points(self, n, xrange, yrange):
        points = []
        x = random.sample(range(xrange), n) #need to use samples or else there can be collisions in the x-axis
        y = random.sample(range(yrange), n)
        for i in range(n):
            points.append((x[i], y[i]))
        return points
    
    def drawPoint(self, canvas,x,y, ram):
        # r = 4
        # id = canvas.create_oval(x-r,y-r,x+r,y+r)
        id = canvas.create_image((x,y),image=ram,state=NORMAL)
        return id
    
    def drawTestHull(self, hull, w, ram):
        hull.append(hull[0])
        for i in range(0, len(hull)-1):
            x, y = hull[i][0], hull[i][1]
            self.drawPoint(w, x, y, ram)
        for i in range(0,len(hull)-1):
            x1 = hull[i][0]
            y1 = hull[i][1]
            x2 = hull[i+1][0]
            y2 = hull[i+1][1]
            w.create_line(x1, y1, x2, y2, width=3)
    
    def test_benchCase(self):
        p = self.points(5, 20, 20)
        start = time.time()
        f = ch.computeHull(p)
        end = time.time()
        print("5 points O(nlogn) time: %f" %(end-start))

        start = time.time()
        h = ch.bruteForce(p)
        end = time.time()
        print("5 points O(n^2): %f" %(end - start))
        self.assertEqual(f, h)

        p = self.points(3, 20, 20)
        start = time.time()
        f = ch.computeHull(p)
        end = time.time()
        print("3 points O(nlogn) time: %f" %(end-start))

        start = time.time()
        h = ch.bruteForce(p)
        end = time.time()
        print("3 points O(n^2): %f" %(end - start))
        self.assertEqual(f, h)

    def test_smallHulls(self):
        p = self.points(10, 800, 800)
        start = time.time()
        f = ch.computeHull(p)
        end = time.time()
        print("10 points O(nlogn) time: %f" %(end-start))

        start = time.time()
        h = ch.bruteForce(p)
        end = time.time()
        print("10 points O(n^2): %f" %(end - start))
        self.assertEqual(f, h)

        p = self.points(50, 800, 800)
        start = time.time()
        f = ch.computeHull(p)
        end = time.time()
        print("50 points O(nlogn) time: %f" %(end-start))

        start = time.time()
        h = ch.bruteForce(p)
        end = time.time()
        print("50 points O(n^2): %f" %(end - start))
        self.assertEqual(f, h)

        p = self.points(100, 800, 800)
        start = time.time()
        f = ch.computeHull(p)
        end = time.time()
        print("100 points O(nlogn) time: %f" %(end-start))

        start = time.time()
        h = ch.bruteForce(p)
        end = time.time()
        print("100 points O(n^2): %f" %(end - start))
        self.assertEqual(f, h)
    
    # def test_visual(self):
    #     p = self.points(500, 999, 799)
    #     f = ch.computeHull(p)
        
    #     master = Tk()

    #     canvas_width = 1000
    #     canvas_height = 800
    #     w = Canvas(master, 
    #             width=canvas_width,
    #             height=canvas_height)
        
    #     laptop = r"E:\Downloads\School\CS\CS 3500\3500-HW\Honors Project\Basic_red_square.png"
    #     pc = r"C:\Users\Zeke\OneDrive\School\CS\CS_3500\3500-HW\Honors Project\oldhusky.gif"
    #     ram = PhotoImage(file=laptop)
    #     submit_button = Button(master, text="Draw Hull", command=self.drawTestHull(f, w, ram))
    #     submit_button.pack()
    #     quit_button = Button(master, text="Quit", command=master.quit)
    #     quit_button.pack()
    #     w.pack()
    #     w.mainloop()
    
    def test_mediumHulls(self):
        p = self.points(1000, 2000, 2000)
        start = time.time()
        f = ch.computeHull(p)
        end = time.time()
        print("1,000 points O(nlogn) time: %f" %(end-start))

        start = time.time()
        h = ch.bruteForce(p)
        end = time.time()
        print("1,000 points O(n^2): %f" %(end - start))
        self.assertEqual(f, h)

        p = self.points(10000, 20000, 20000)
        start = time.time()
        f = ch.computeHull(p)
        end = time.time()
        print("10,000 points O(nlogn) time: %f" %(end-start))

        start = time.time()
        h = ch.bruteForce(p)
        end = time.time()
        print("10,000 points O(n^2): %f" %(end - start))
        self.assertEqual(f, h)
    
    def test_largeHulls(self):
        p = self.points(100000, 200000, 200000)
        start = time.time()
        f = ch.computeHull(p)
        end = time.time()
        print("100,000 points O(nlogn) time: %f" %(end-start))

        start = time.time()
        h = ch.bruteForce(p)
        end = time.time()
        print("100,000 points O(n^2): %f" %(end - start))
        self.assertEqual(f, h)

        p = self.points(500000, 600000, 600000)
        start = time.time()
        f = ch.computeHull(p)
        end = time.time()
        print("500,000 points O(nlogn) time: %f" %(end-start))

        start = time.time()
        h = ch.bruteForce(p)
        end = time.time()
        print("500,000 points O(n^2): %f" %(end - start))
        self.assertEqual(f, h)

        p = self.points(1000000, 2000000, 2000000)
        start = time.time()
        f = ch.computeHull(p)
        end = time.time()
        print("1,000,000 points O(nlogn) time: %f" %(end-start))

        start = time.time()
        h = ch.bruteForce(p)
        end = time.time()
        print("1,000,000 points O(n^2): %f" %(end - start))
        self.assertEqual(f, h)

        p = self.points(5000000, 6000000, 6000000)
        start = time.time()
        f = ch.computeHull(p)
        end = time.time()
        print("5,000,000 points O(nlogn) time: %f" %(end-start))

        start = time.time()
        h = ch.bruteForce(p)
        end = time.time()
        print("5,000,000 points O(n^2): %f" %(end - start))
        self.assertEqual(f, h)


        

class TestHelperFunctions(unittest.TestCase):

    # def test_Tangent(self):
    #     ch.tangent()
    

    def test_rightMostIndex(self):
        pass




if __name__ == "__main__":
    unittest.main()