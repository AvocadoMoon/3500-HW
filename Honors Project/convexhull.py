import math
import sys

EPSILON = sys.float_info.epsilon

'''
Given two points, p1 and p2,
an x coordinate, x,
and y coordinates y3 and y4,
compute and return the (x,y) coordinates
of the y intercept of the line segment p1->p2
with the line segment (x,y3)->(x,y4)
'''
# shoudl be used to see if point a + 1, b + 1, a - 1, and b - 1 to make sure it does not intercept with the
# tangent line, input a + 1 x cord for x, region between the two points for y3, y4
# if the y point from this function is equivelant to the y point of a + 1 then it is known an interception happens
# and can not use that tangent  
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
#helper function for cw, ccw, and collinear
def triangleArea(a, b, c):
	return (a[0]*b[1] - a[1]*b[0] + a[1]*c[0] \
                - a[0]*c[1] + b[0]*c[1] - c[0]*b[1]) / 2.0;


#check if a-1 -> a -> a+1 are clockwise
'''
Given three points a,b,c,
returns True if and only if 
a,b,c represents a clockwise sequence
(subject to floating-point precision)
'''
def cw(a, b, c):
	return triangleArea(a,b,c) < EPSILON;
'''
Given three points a,b,c,
returns True if and only if 
a,b,c represents a counter-clockwise sequence
(subject to floating-point precision)
'''
def ccw(a, b, c):
	return triangleArea(a,b,c) > EPSILON;

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

class Line():
	def __init__(self, a, b):
		self.a = a
		self.b = b
		self.m = 0
		self.yInt = 0
		self.slope(a, b)
		self.yIntercept(a, self.m)
	
	def slope(self, a, b):
		self.m = (a[1] - b[1]) / (a[0] - b[0])

	def yIntercept(self, a, m):
		self.yInt = a[1] - (m * a[0])

	def pointSlope(self, x):
		y = ((self.m*x) + self.yInt)
		return y
	
	def pointSlopeY(self, y):
		x = (y - self.yInt) / self.m
		return x

#determines whether a point is within the area
def inBetween(upper, leftSide, lower, rightSide, point):
	# yT = upper.pointSlope(point[0]) #ytop at the points x
	# yB = lower.pointSlope(point[0])
	xL = leftSide.pointSlopeY(point[1])
	xR = rightSide.pointSlopeY(point[1])
	if (xL < point[0]) and (point[0] < xR):
		return True
	return False

def tangent(mPoint, oPoint, set, mIndex, upper=True):
	n = (mIndex + 1) % len(set)
	z1 = set[n]
	n = (mIndex - 1) % len(set)
	z1n = set[n]
	line = Line(mPoint, oPoint)
	y1 = line.pointSlope(z1[0])
	y1n = line.pointSlope(z1n[0])

	#really just need to check if the points +- are both either above or below the tangent line which getting the actal slope formula for the line helps a lot
	if upper:
		if (y1 > z1[1]) or (y1n > z1n[1]):
			return False
		return True
	if not upper:
		if (y1 < z1[1]) or (y1n < z1n[1]):
			return False
		return True
			
	

'''
Replace the implementation of computeHull with a correct computation of the convex hull
using the divide-and-conquer algorithm. Must return points in clockwise order for drawing purposes.
'''
def computeHull(points):
	if len(points) > 3:
		mid = len(points) //2
		A, asort = computeHull(points[:mid])
		B, bsort = computeHull(points[mid:])

		#sort the points by x cords
		# while len(A) !=0 and len(B) != 0:
		# 	if A[0][0] > B[0][0]:
		# 		sort.append(B[0])
		# 		B.pop(0)
		# 		if len(B == 0):
		# 			sort.extend(A)
		# 	else:
		# 		sort.append(A[0])
		# 		A.pop(0)
		# 		if len(A == 0):
		# 			sort.extend(A)
		
		# needed sorted x list to find the rightmost or leftmost point in either A or B
		# then the clockwise sort is needed because of rotating through the hull
		ai = len(asort) - 1
		bi = 0
		aUpper, aLower = asort[ai], asort[ai]
		bUpper, bLower = bsort[bi], bsort[bi]
		ai = A.index(aUpper)
		bi = B.index(bUpper)


		#gets upper tangent
		while not(tangent(aUpper, bUpper, A, ai, True)) and not(tangent(bUpper, aUpper, B, bi, True)):
			while not(tangent(aUpper, bUpper, A, ai, True)):
				ai = (ai + 1) % len(A)
				aUpper = A[ai]
			while not(tangent(bUpper, aUpper, B, bi, True)):
				bi = (bi - 1) % len(B)
				bUpper = B[bi]

		#gets lower tangent
		while not(tangent(aLower, bLower, A, ai, False)) and not(tangent(bLower, aLower, B, bi, False)):
			while not(tangent(aLower, bLower, A, ai, False)):
				ai = (ai - 1) % len(A)
				aLower = A[ai]
			while not(tangent(bLower, aLower, B, bi, False)):
				bi = (bi + 1) % len(B)
				bLower = B[bi]
		
		upperLine = Line(aUpper, bUpper)
		lowerLine = Line(aLower, bLower)
		aa = Line(aUpper, aLower)
		bb = Line(bUpper, bLower)


		hull = [f for f in points if not(inBetween(upperLine, aa, lowerLine, bb, f))] #need to continue working on this

		xsort = sorted(hull, key=lambda p: p[0])
		clockwiseSort(hull)
		return hull, xsort
		#need to figure out what to do with these tangents, and how to implement them within the united set
		# maybe ever point past the x point from the newly made tangent then get ride of from hull
	else:
		xsort = sorted(points, key=lambda p: p[0])
		#xsort = points.sort(key = lambda p: p[0])
		clockwiseSort(points)
		return points, xsort
	# print(points)
	# clockwiseSort(points)
	# print(points)
	# return points

'''
FACTS:

Points that get returned are part of the current hull, not the whole set of points will be returned.
No three points forming the hull can be colinear.
No two points are on a vertical line
'''

'''
Intial sorting of list takes O(nlogn) time plus the O(n/2) time for going through the list and inching down to lowest tangential
Split the list of points into smallest list possible, set of 2
Afterwards, while merging sort the lists, this should take O(n) time, in addition after sort
then compute the lowest tangent possible for that set taking another O(n) time. In total it sould be
T(n) = 2T(n/2) + O(n) + O(n) => T(n) = 2T(n/2) + O(2n)

Finding the low
'''

'''
A convex hull is the smallest possible polygonal shape that can envelope some points within a graph.
So by finding the convex hull at step i, all that is needed to know the convex hull at step i+1 is a lower tangential line that
connects the two convex hulls and an upper line that connects the two convex hulls. Now those two convex hulls become one large convex hull.

Smallest possible convex hull would be a triangle since it only contains three points, yet still creats a geometric shape
'''