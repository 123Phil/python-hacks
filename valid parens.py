# Phillip Stewart
# A python version of the codeEval challenge
# uses a dictionary and treats a list like a stack

import sys

def main(args):
	if len(args) != 2:
		print 'Usage ~: ' + args[0] + ' filename.txt'
		sys.exit(0)
	else:
		filename = args[1]
	
	D = { ')':'(' , '}':'{' , ']':'[' }
	P = [ '(','{','[' ]
	
	with open(filename, 'r') as f:
		for line in f:
			if line.strip() == '':
				continue
			parens = []
			for character in list(line.strip()):
				if character in P:
					parens.append(character)
				elif character in D:
					if parens[-1] == D[character]:
						del parens[-1]
					else:
						print 'False'
						break
			else:
				print 'True'


if __name__ == "__main__":
	main(sys.argv)
