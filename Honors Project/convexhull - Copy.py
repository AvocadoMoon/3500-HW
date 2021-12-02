import math
import sys
from tkinter.constants import NO, RIGHT

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


def leftMostIndex(points):
    minn = 0

    for i in range(1,len(points)):
        if points[i][0] < points[minn][0]:
            minn = i
        elif points[i][0] == points[minn][0]:
            if points[i][1] > points[minn][1]:
                minn = i
    return minn


def rightMostIndex(points):
	maxx = 0

	for i in range(1, len(points)):
		if points[i][0] > points[maxx][0]:
			maxx = i
		elif points[i][0] == points[maxx][0]:
			if points[i][1] > points[maxx][1]:
				maxx = i
		return maxx


#B and counterclockwise means going down
#A and clockwise means going down
def tangent(a, b, c, A=True, upper=True):
	if (A and upper) or (not(A) and not(upper)):
		return ccw(a, b, c)
	elif (A and not(upper)) or (not(A) and upper):
		return cw(a, b , c)
	

'''
Replace the implementation of computeHull with a correct computation of the convex hull
using the divide-and-conquer algorithm. Must return points in clockwise order for drawing purposes.
'''
def computeHull(points):
	if (len(points) > 5):
		mid = len(points) // 2
		A = computeHull(points[:mid])
		B = computeHull(points[mid:])

		ai = rightMostIndex(A)
		bi = leftMostIndex(B)

		aUpper, bUpper = 0, 0
		ain = ai
		bin = bi

		done = 0
		while(not(done)):
			done = 1

			while (tangent(B[bin], A[ain], A[(ain+1) % len(A)], True, True)):
				ain = (ain + 1) % len(A)
			
			while (tangent(A[ain], B[bin], B[(bin-1) % len(B)], False, True)):
				bin = (bin - 1) % len(B)
				done = 0
		
		aUpper, bUpper = ain, bin
		done = 0
		ain, bin = ai, bi
		while(not(done)):
			done = 1

			while (tangent(B[bin], A[ain], A[(ain-1) % len(A)], True, False)):
				ain = (ain - 1) % len(A)
			
			while (tangent(A[ain], B[bin], B[(bin+1) % len(B)], False, False)):
				bin = (bin + 1) % len(B)
				done = 0
		
		aLower, bLower = ain, bin
		hull = []
		ind = aLower
		hull.append(A[aLower])
		while(ind != aUpper):
			ind = (ind + 1) % len(A)
			hull.append(A[ind])
		
		ind = bLower
		hull.append(B[bLower])
		while(ind != bUpper):
			ind = (ind + 1) % len(B)
			hull.append(B[ind])

		return hull
	else:
		return bruteForce(points)


def bruteForce(points):
	n = len(points)
	if n < 3:
		return
 
    # Find the leftmost point
	l = leftMostIndex(points)
 
	hull = []
     
	'''
    Start from leftmost point, keep moving counterclockwise
    until reach the start point again. This loop runs O(h)
    times where h is number of points in result or output.
    '''
	p = l
	q = 0
	while(True):
         
        # Add current point to result
		hull.append(points[p])
 
		'''
        Search for a point 'q' such that orientation(p, q,
        x) is counterclockwise for all points 'x'. The idea
        is to keep track of last visited most counterclock-
        wise point in q. If any point 'i' is more counterclock-
        wise than q, then update q.
        '''
		q = (p + 1) % n
 
		for i in range(n):
             
			# If i is more counterclockwise
            # than current q, then update q
			if(ccw(points[p],points[i], points[q])):
				q = i

		'''
        Now q is the most counterclockwise with respect to p
        Set p as q for next iteration, so that q is added to
        result 'hull'
        '''
		p = q
 
		# While we don't come to first point
		if(p == l):
			break
	clockwiseSort(hull)
	return hull

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