# Phillip Stewart
# pascal's triangle codeEval challenge

import sys

def fact(i):
	prod = 1
	while i > 1:
		prod *= i
		i -= 1
	return prod


def pascal(row, i):
	return fact(row)/(fact(i)*fact(row-i))


def main(args):
	if len(args) != 2:
		print 'Usage ...'
		sys.exit(0)
	else:
		filename = args[1]
	
	with open(filename, 'r') as f:
		for line in f:
			num = int(line.strip())
			for row in xrange(0,num):
				for i in xrange(0,row+1):
					print pascal(row,i),
			print ''


if __name__ == "__main__":
	main(sys.argv)
