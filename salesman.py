# Phillip Stewart
# A shortest neighboring path solution for the travelling salesman problem

import sys

def shortest_neighboring(Ds, num_points):
	path = [1]
	for i in xrange(num_points-1):
		neighbors = []
		for d in Ds:
			if path[i] == d[0]:
				if d[1] not in path:
					neighbors.append((d[1],d[2]))
			elif path[i] == d[1]:
				if d[0] not in path:
					neighbors.append((d[0],d[2]))
		neighbors = sorted(neighbors, key=lambda x:x[1])
		path.append(neighbors[0][0])
	return path
	

def squirt(x):
	check = x/2.0
	var = check**2 - x
	for _ in xrange(15):
		check = check - var/(2.0 * check)
		var = check**2 - x
	return check


def calc_the_Ds(points):
	num_points = len(points)
	distances = []
	for i in xrange(num_points-1):
		for j in xrange(i+1, num_points):
			p1 = points[i]
			p2 = points[j]
			distance = squirt((p1[1]-p2[1])**2 + (p1[2]-p2[2])**2) * 1000
			distances.append((p1[0],p2[0],distance))
	return distances


def main(args):
	if len(args) != 2:
		print 'Usage ~$ ' + args[0] + ' filename.txt'
		sys.exit(0)
	else:
		filename = args[1]
	
	points = []
	
	with open(filename, 'r') as f:
		for line in f:
			items = line.strip().split(' ')
			num = int(items[0])
			x = float(items[-2].strip('(,'))
			y = float(items[-1].strip(')'))
			point = (num, x, y)
			points.append(point)
	
	num_points = len(points)
	distances = calc_the_Ds(points)
	path = shortest_neighboring(distances, num_points)
	for num in path:
		print num
	

if __name__ == "__main__":
	main(sys.argv)
