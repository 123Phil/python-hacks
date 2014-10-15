# Phillip Stewart
# another codeEval challenge
# I think this one prints the words
# for integers given
# with 'dollars' on the end

import sys


def printDollar(num):
	d = {0:'Zero',1:'One',2:'Two',3:'Three',4:'Four',5:'Five'
			,6:'Six',7:'Seven',8:'Eight',9:'Nine'}
	d2 = {1:'Ten',2:'Twenty',3:'Thirty',4:'Forty',5:'Fifty'
			,6:'Sixty',7:'Seventy',8:'Eighty',9:'Ninety'}
	
	words = []
	dec = 1000000000
	i = 0
	while(num >= dec):
		i += 1
		num -= dec
	if i > 0:
		words.append(d[i])
		words.append('Billion')
	dec /= 10
	
	i = 0
	didAppend = 0
	while(num >= dec):
		i += 1
		didAppend += 1
		num -= dec
	if i > 0:
		words.append(d[i])
		words.append('Hundred')
	dec /= 10
	i = 0
	while(num >= dec):
		i += 1
		didAppend += 1
		num -= dec
	if i > 0:
		words.append(d2[i])
	dec /= 10
	i = 0
	while(num >= dec):
		i += 1
		didAppend += 1
		num -= dec
	if i > 0:
		words.append(d[i])
	dec /= 10
	if didAppend:
		words.append('Million')
		
	i = 0
	didAppend = 0
	while(num >= dec):
		i += 1
		didAppend += 1
		num -= dec
	if i > 0:
		words.append(d[i])
		words.append('Hundred')
	dec /= 10
	i = 0
	while(num >= dec):
		i += 1
		didAppend += 1
		num -= dec
	if i > 0:
		words.append(d2[i])
	dec /= 10
	i = 0
	while(num >= dec):
		i += 1
		didAppend += 1
		num -= dec
	if i > 0:
		words.append(d[i])
	dec /= 10
	if didAppend:
		words.append('Thousand')
	
	i = 0
	didAppend = 0
	while(num >= dec):
		i += 1
		didAppend += 1
		num -= dec
	if i > 0:
		words.append(d[i])
		words.append('Hundred')
	dec /= 10
	i = 0
	while(num >= dec):
		i += 1
		didAppend += 1
		num -= dec
	if i > 0:
		words.append(d2[i])
	dec /= 10
	i = 0
	while(num >= dec):
		i += 1
		didAppend += 1
		num -= dec
	if i > 0:
		words.append(d[i])
	
	words.append('Dollars')
	print ''.join(words)
		

def main(args):
	if len(args) != 2:
		print 'Usage ...'
		sys.exit(0)
	else:
		filename = args[1]
	
	
	with open(filename, 'r') as f:
		for line in f:
			num = int(line.strip())
			printDollar(num)


if __name__ == "__main__":
	main(sys.argv)
