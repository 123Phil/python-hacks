# Phillip Stewart

from sys import argv

scriptname = argv[0]

if len(argv) != 3:
	print "Usage: " + scriptname + " filename.ext spacesPerTab"
	print "  Where filename.ext is a file with spacing/indent issues"
	print "  And spacesPerTab is the number of spaces to replace per tab"

filename = argv[1]
spacesPerTab = int(argv[2])

with open(filename, 'r') as filehandle:
	lines = filehandle.readlines()

lines2 = []
for line in lines:
	numSpaces = 0
	for letter in line:
		if letter is ' ':
			numSpaces += 1
		else:
			break
	numTabs = numSpaces / spacesPerTab
	line = line[numSpaces:]
	for unused in xrange(numTabs):
		line = '\t' + line
	lines2.append(line)

text = ''.join(lines2)
newfilename = 'Tabbed Copy of ' + filename

with open(newfilename, 'w') as newfilehandle:
	newfilehandle.write(text)

