import convexhull as ch
import unittest
import random
from tkinter import *
import time

class TestHull(unittest.TestCase):

    def time(self, brute, n, p):
        if brute:
            start = time.time()
            h = ch.bruteForce(p)
            end = time.time()
            print("{} points O(n^2): {:.5f}".format(n, (end - start)))
            return h
        else:
            start = time.time()
            h = ch.computeHull(p)
            end = time.time()
            print("{} points O(nLogn): {:.5f}".format(n, (end - start)))
            return h

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
        n = 5
        p = self.points(n, n*10, n*10)
        f = self.time(False, n, p)
        h = self.time(True, n, p)
        self.assertEqual(f, h)

        n = 4
        p = self.points(n, n*10, n*10)
        f = self.time(False, n, p)
        h = self.time(True, n, p)
        self.assertEqual(f, h)

        n = 3
        p = self.points(n, n*10, n*10)
        f = self.time(False, n, p)
        h = self.time(True, n, p)
        self.assertEqual(f, h)

    # def test_smallHulls(self):
    #     n = 10
    #     p = self.points(n, n*10, n*10)
    #     f = self.time(False, n, p)
    #     h = self.time(True, n, p)
    #     self.assertEqual(f, h)

    #     n = 50
    #     p = self.points(n, n*10, n*10)
    #     f = self.time(False, n, p)
    #     h = self.time(True, n, p)
    #     self.assertEqual(f, h)

    #     n = 100
    #     p = self.points(n, n*10, n*10)
    #     f = self.time(False, n, p)
    #     h = self.time(True, n, p)
    #     self.assertEqual(f, h)
    
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
    
    # def test_mediumHulls(self):
    #     n = 1000
    #     p = self.points(n, n*2, n*2)
    #     f = self.time(False, n, p)
    #     h = self.time(True, n, p)
    #     self.assertEqual(f, h)

    #     n = 10000
    #     p = self.points(n, n*2, n*2)
    #     f = self.time(False, n, p)
    #     h = self.time(True, n, p)
    #     self.assertEqual(f, h)
    
    # def test_largeHulls(self):
    #     n = 100000
    #     p = self.points(n, (n + (n//2)), (n + (n//2)))
    #     f = self.time(False, n, p)
    #     h = self.time(True, n, p)
    #     self.assertEqual(f, h)

    #     n = 500000
    #     p = self.points(n, (n + (n//2)), (n + (n//2)))
    #     f = self.time(False, n, p)
    #     h = self.time(True, n, p)
    #     self.assertEqual(f, h)

    #     n = 1000000
    #     p = self.points(n, (n + (n//2)), (n + (n//2)))
    #     f = self.time(False, n, p)
    #     h = self.time(True, n, p)
    #     self.assertEqual(f, h)

    #     n = 5000000
    #     p = self.points(n, (n + (n//2)), (n + (n//2)))
    #     f = self.time(False, n, p)
    #     h = self.time(True, n, p)
    #     self.assertEqual(f, h)




if __name__ == "__main__":
    unittest.main()