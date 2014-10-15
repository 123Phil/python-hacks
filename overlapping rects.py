# Phillip Stewart
# another codeEval challenge
# detemines whether given rectangles are overlapping

import sys

def InBox(point, box):
	left_x,top_y,right_x,bottom_y = box
	x,y = point
	if (x >= left_x and x <= right_x) and (y >= bottom_y and y <= top_y):
		return True
	else:
		return False
	

def EdgePoints(box):
	points = []
	left_x,top_y,right_x,bottom_y = box
	for i in xrange(left_x,right_x + 1):
		points.append( (i, top_y) )
		points.append( (i, bottom_y) )
	for i in xrange(bottom_y + 1, top_y):
		points.append( (left_x, i) )
		points.append( (right_x, i) )
	return points
		

def Inside(A, B):#just in-case A is entirely contained in B
	if A[0]>B[0] and A[1]<B[1] and A[2]<B[2] and A[3]>B[3]:
		return True
	else:
		return False


def Isect(A, B):
	b_points = EdgePoints(B)
	if Inside(A, B):
		return True
	for point in b_points:
		if InBox(point, A):
			return True
	else:
		return False


def main(args):
	if len(args) != 2:
		print 'Usage ~$ ' + args[0] + ' filename.txt'
		sys.exit(0)
	else:
		filename = args[1]
	
	with open(filename, 'r') as f:
		for line in f:
			nums = line.strip().split(',')
			A = [int(x) for x in nums[:4]]
			B = [int(x) for x in nums[4:]]
			
			print Isect(A,B)


if __name__ == "__main__":
	main(sys.argv)
