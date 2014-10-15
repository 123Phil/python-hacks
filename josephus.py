# Phillip Stewart
# Josephus codeEval challenge

import sys


def main(args):
	if len(args) != 2:
		print 'Usage ~$ ' + args[0] + ' filename.txt'
		sys.exit(0)
	else:
		filename = args[1]
	
	with open(filename, 'r') as f:
		for line in f:
			n,m = (int(x) for x in line.strip().split(','))
			soldiers = range(n)
			m -= 1
			index = m
			while n > 1:
				print soldiers[index],
				del soldiers[index]
				n -= 1
				index = (index + m) % n
			print soldiers[0]


if __name__ == "__main__":
	main(sys.argv)
