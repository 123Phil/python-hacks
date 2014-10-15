# Phillip Stewart
# ever run into problems with spaces and tabs in a .py file?
# yeah, that shit sucks...
# so here's a python file that can set you straight.
# everyone should use tabs -
# in most editors, you can set tab width to whatever you'd like,
# so use tabs and set to your preference
# no need for 2 space/4 space garbage that is hard to navigate through...
# tabbify your shit right away with this simple tool!

import sys

SPACE_PER_TAB = 4

def main(args):
	if len(args) != 2:
		print 'Usage ~$ ' + args[0] + ' filename.txt'
		sys.exit(0)
	else:
		filename = args[1]
	
	outfile = ''
	if filename[-4] == '.':
		outfile = filename[:-4] + ' tabbed' + filename[-4:]
	elif '/' in filename:
		outfile = filename + 'TAB'
	else:
		outfile = 'tabbed ' + filename
	
	out = open(outfile, 'w')
	with open(filename, 'r') as f:
		bad_lines = 0
		for line in f:
			spaces = 0
			for letter in line:
				if letter == ' ':
					spaces += 1
				else:
					break
			if spaces%SPACE_PER_TAB == 0:
				tabs = spaces / SPACE_PER_TAB
				line = '\t'*tabs + line[spaces:]
			else:
				bad_lines += 1
			out.write(line)
		if bad_lines > 0:
			print bad_lines, 'lines contained prefix spaces indivisible by', SPACE_PER_TAB
	out.close()

if __name__ == "__main__":
	main(sys.argv)
