# Phillip Stewart
# CodeEval challenge: https://www.codeeval.com/open_challenges/57/
# Given m;n;[m*n elems] it gives the elements back
# in order along a spiral starting at the top left going clockwise.

import sys

def spiral(n, m):
	indys = []
	nctr,mctr = n,m
	i = -1
	while mctr > 0:
		for _ in xrange(mctr):
			i += 1
			indys.append(i)
		nctr -= 1
		if nctr == 0:
			break
		for _ in xrange(nctr):
			i += m
			indys.append(i)
		mctr -= 1
		if mctr == 0:
			break
		for _ in xrange(mctr):
			i -= 1
			indys.append(i)
		nctr -= 1
		if nctr == 0:
			break
		for _ in xrange(nctr):
			i -= m
			indys.append(i)
		mctr -= 1
	return indys
		

def main(args):
	if len(args) != 2:
		print 'Usage ~$ ' + args[0] + ' filename.txt'
		sys.exit(0)
	else:
		filename = args[1]
	
	
	with open(filename, 'r') as f:
		for line in f:
			n,m,elems = line.strip().split(';')
			n = int(n)
			m = int(m)
			elems = elems.split(' ')
			
			indexs = spiral(n, m)
			for i in indexs:
				print elems[i],
			print ''
						


if __name__ == "__main__":
	main(sys.argv)
