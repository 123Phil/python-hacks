# Phillip Stewart
# Determines if 4 points define a square.
# the algorithm here is simple:
# find the distance between the set of points
# four of those distances should be equal - sides of the square
# the diagonals should be equal to eachother,
# and equal to the square root of double the square of a side

# for some reason I used my squirt function instead of math.sqrt here...

import sys


def squirt(x):
	check = x/2.0
	var = check**2 - x
	for _ in xrange(15):
		check = check - var/(2.0 * check)
		var = check**2 - x
	return check


def getD(points):
	num_points = 4
	distances = []
	for i in xrange(num_points-1):
		for j in xrange(i+1, num_points):
			p1 = points[i]
			p2 = points[j]
			distance = squirt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)
			distances.append(distance)
	return sorted(distances)


def isSquare(points):
	dists = getD(points)
	cross = round(squirt(2*(dists[0]**2)), 2)
	dists = [round(x, 2) for x in dists]
	if dists[0] == dists[1] == dists[2] == dists[3] and cross == dists[4] == dists[5]:
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
			points = []
			items = line.strip().split(', ')
			for item in items:
				x,y = [int(a) for a in item.strip('()').split(',')]
				points.append((x,y))
			
			if isSquare(points):
				print 'true'
			else:
				print 'false'
	

if __name__ == "__main__":
	main(sys.argv)
