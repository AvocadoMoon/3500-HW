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

def tangent(a, b, A, B, ai, bi, upperOrLower):
	def intercept(index, set, mPoint, point, i):
		n = (index + i) % len(set)
		n = set[n]
		return yint(mPoint, point, n[0], mPoint[1], point[1]), n[1]
	aXP, aYP, aP = intercept(ai, A, a, b, 1)
	aXN, aYN, aN = intercept(ai, A, a, b, -1)
	bXP, bYP, bP = intercept(bi, B, b, a, 1)
	bXN, bYN, bN = intercept(bi, B, b, a, -1)

	#if any of the tangents intersect their own shape then it can not be the lowest tangent, may have to do only for A set idk if I have to do it for B
	if (aYP == aP) or (aYN == aN) or (bYP == bP) or (bYN == bN):
		return False

'''
Replace the implementation of computeHull with a correct computation of the convex hull
using the divide-and-conquer algorithm. Must return points in clockwise order for drawing purposes.
'''
def computeHull(points):
	if len(points) != 2:
		mid = len(points) //2
		A = computeHull(points[:mid])
		B = computeHull(points[mid:])
		sort = []

		#sort the points by x cords
		while len(A) !=0 and len(B) != 0:
			if A[0][0] > B[0][0]:
				sort.append(B[0])
				B.pop(0)
				if len(B == 0):
					sort.extend(A)
			else:
				sort.append(A[0])
				A.pop(0)
				if len(A == 0):
					sort.extend(A)
		
		a = A[-1]
		b = B[0]

		

		
		
	else:
		if points[0][0] > points[1][0]:
			points[0], points[1] = points[1], points[0]
			return points
		return points
	print(points)
	#clockwiseSort(points)
	print(points)
	return points

'''
FACTS:

Points that get returned are part of the current hull, not the whole set of points will be returned.
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

x, y = yint((1,1), (4,5), 3, 0, 4)
print(x, y)