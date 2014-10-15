# careful with this one...
import os
i = 1
for fn in os.listdir('.'):
	print fn, "Title S01" + "{0:02d}".format(i) + fn[-4:]
#	os.rename(fn, "Title S01" + "{0:02d}".format(i) + fn[-4:])
	i += 1
