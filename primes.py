# Phil
#
# For CodeEval challenge - https://www.codeeval.com/open_challenges/46/
# Prints primes up to number given for line in file


import sys


def primeList(max):
	primes = []
	if (max < 2):
		return primes
	else:
		primes.append(2)
	for i in xrange(3, max+1, 2):
		for prime in primes:
			if (i%prime == 0):
				break
		else:
			primes.append(i)
	return primes


def main(args):
	filename = ''
	lines = []
	
	if (len(args) != 2):
		print "Usage: ~$ " + str(args[0]) + " filename.txt"
		sys.exit(0)
	else:
		filename = str(args[1])
	
	
	with open(filename, 'r') as f:
		for line in f:
			lines.append(int(line))

	highest = max(lines)
	p_list = primeList(highest)
	
	for num in lines:
		p_out = []
		for i in p_list:
			if i < num:
				p_out.append(i)
			else:
				break
		print ','.join(str(x) for x in p_out)
		


if __name__ == "__main__":
	main(sys.argv)
