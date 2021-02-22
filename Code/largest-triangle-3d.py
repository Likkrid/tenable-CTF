#!/usr/bin/env python3

import itertools

def heron(a,b,c):
    s = (a + b + c) / 2
    area = (s*(s-a) * (s-b)*(s-c)) ** 0.5
    return area

def distance3d(x1,y1,z1,x2,y2,z2):
    a=(x1-x2)**2+(y1-y2)**2 + (z1-z2)**2
    d= a ** 0.5
    return d

def areatriangle3d(points_tuple):
	x1, y1, z1 = points_tuple[0]
	x2, y2, z2 = points_tuple[1]
	x3, y3, z3 = points_tuple[2]
	a=distance3d(x1,y1,z1,x2,y2,z2)
	b=distance3d(x2,y2,z2,x3,y3,z3)
	c=distance3d(x3,y3,z3,x1,y1,z1)
	A = heron(a,b,c)
	return A

def FindLargestTriangleArea(points):
	largest = 0
	tuples = list(itertools.combinations(points, 3))

	for p_tuple in tuples:
		candidate = areatriangle3d(p_tuple)
		if candidate > largest:
			largest = candidate
	return largest

points_data = "-21,59,-93 -4,91,-2 1,61,2, 0,44,1"
#points_data = raw_input()
points = []
for point in points_data.split(' '):
  point_xyz = point.split(',')
  points.append([int(point_xyz[0]), int(point_xyz[1]), int(point_xyz[2])])

# Compute Largest Triangle and Print Area rounded to nearest whole number
area = FindLargestTriangleArea(points)
print (int(round(area)))
