import math
import sys
from tkinter.constants import RIGHT

EPSILON = sys.float_info.epsilon

'''
Given two points, p1 and p2,
an x coordinate, x,
and y coordinates y3 and y4,
compute and return the (x,y) coordinates
of the y intercept of the line segment p1->p2
with the line segment (x,y3)->(x,y4)
'''

def yint(p1, p2, x, y3, y4):
	x1, y1 = p1
	x2, y2 = p2
	x3 = x
	x4 = x
	px = ((x1*y2 - y1*x2) * (x3 - x4) - (x1 - x2)*(x3*y4 - y3*x4)) / \
		 float((x1 - x2)*(y3 - y4) - (y1 - y2)*(x3 - x4))
	py = ((x1*y2 - y1*x2)*(y3-y4) - (y1 - y2)*(x3*y4 - y3*x4)) / \
			float((x1 - x2)*(y3 - y4) - (y1 - y2)*(x3-x4))
	return (px, py)

'''
Given three points a,b,c,
computes and returns the area defined by the triangle
a,b,c. 
Note that this area will be negative 
if a,b,c represents a clockwise sequence,
positive if it is counter-clockwise,
and zero if the points are collinear.
'''

def triangleArea(a, b, c):
	res = (b[1] - a[1]) * (c[0] - b[0]) - (c[1] - b[1]) * (b[0] - a[0])
	return res

'''
Given three points a,b,c,
returns True if and only if 
a,b,c represents a clockwise sequence
(subject to floating-point precision)
'''
def cw(a, b, c):
	return triangleArea(a,b,c) < EPSILON
'''
Given three points a,b,c,
returns True if and only if 
a,b,c represents a counter-clockwise sequence
(subject to floating-point precision)
'''
def ccw(a, b, c):
	return triangleArea(a,b,c) > EPSILON

'''
Given three points a,b,c,
returns True if and only if 
a,b,c are collinear
(subject to floating-point precision)
'''
def collinear(a, b, c):
	return abs(triangleArea(a,b,c)) <= EPSILON

'''
Given a list of points,
sort those points in clockwise order
about their centroid.
Note: this function modifies its argument.
'''
def clockwiseSort(points):
	# get mean x coord, mean y coord
	xavg = sum(p[0] for p in points) / len(points)
	yavg = sum(p[1] for p in points) / len(points)
	angle = lambda p:  ((math.atan2(p[1] - yavg, p[0] - xavg) + 2*math.pi) % (2*math.pi))
	points.sort(key = angle)


#O(n) time
def leftMostIndex(points):
    minn = 0
    for i in range(1,len(points)):
        if points[i][0] < points[minn][0]:
            minn = i
    return minn


#O(n) time
def rightMostIndex(points):
	maxx = 0
	for i in range(1, len(points)):
		if points[i][0] > points[maxx][0]:
			maxx = i
	return maxx


#B and counterclockwise means going down
#A and clockwise means lower tangent
def tangent(a, b, c, A=True, upper=True):
	if (A and upper) or (not(A) and not(upper)):
		res = ccw(a, b, c)
		return res
	elif (A and not(upper)) or (not(A) and upper):
		return cw(a, b , c)
	

'''
Replace the implementation of computeHull with a correct computation of the convex hull
using the divide-and-conquer algorithm. Must return points in clockwise order for drawing purposes.
'''

def computeHull(points):
	points.sort(key= lambda p: p[0]) #O(nLog(n)) to intially sort the list by x coordinate
	h = ch(points) #O(nLog(n)) to create convex hull
	clockwiseSort(h) #O(nLog(n)) to sort convex hull in clockwise order
	return h


def ch(points):
	if (len(points) > 5):
		#divides hull unitl each hull is 3-5 points
		mid = len(points) // 2
		A = computeHull(points[:mid])
		B = computeHull(points[mid:])

		ai = rightMostIndex(A)
		bi = leftMostIndex(B)

		aUpper, bUpper = 0, 0
		ain = ai
		bin = bi

		done = 0
		#upper tangent
		while(not(done)):
			done = 1

			#A upper should be ccw
			while (not(ccw(B[bin], A[ain], A[(ain-1) % len(A)]))): #a needs to move counter clockwise so a-1 mod len
				ain = (ain - 1) % len(A)
			
			#B upper should be cw
			while (not(cw(A[ain], B[bin], B[(bin+1) % len(B)]))): #b needs to move clockwise to go up
				bin = (bin + 1) % len(B)
				done = 0
		
		aUpper, bUpper = ain, bin
		done = 0
		ain, bin = ai, bi

		#lower tangent
		while(not(done)):
			done = 1

			#A lower should be cw
			while (not(cw(B[bin], A[ain], A[(ain+1) % len(A)]))):
				ain = (ain + 1) % len(A)
			
			#B lower should be ccw
			while (not(ccw(A[ain], B[bin], B[(bin-1) % len(B)]))):
				bin = (bin - 1) % len(B)
				done = 0
		
		aLower, bLower = ain, bin
		hull = []
		ind = aLower
		hull.append(A[aLower])
		#adds to finished hull the left hull, A, in clockwise order
		while(ind != aUpper):
			ind = (ind + 1) % len(A)
			hull.append(A[ind])
		
		ind = bUpper
		hull.append(B[bUpper])
		#adds to finished hull the right hull, B, in clockwise order
		while(ind != bLower):
			ind = (ind + 1) % len(B)
			hull.append(B[ind])
		return hull
	else:
		#for the small hulls brute force is extremely quick and does not make the overall time much slower
		return bruteForce(points)

def bruteForce(points):
	n = len(points)
	if n < 3:
		return
    # Find the leftmost point
	l = leftMostIndex(points)
	hull = []
	p = l
	q = 0

	while(True):
        # Add current point to result
		hull.append(points[p])
		q = (p + 1) % n

		for i in range(n):
			# If i is more counterclockwise
            # than current q, then update q
			if(ccw(points[p],points[i], points[q])):
				q = i
				
		p = q
		# While we don't come to first point
		if(p == l):
			break
	clockwiseSort(hull)
	return hull