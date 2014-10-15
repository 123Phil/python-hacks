# Phillip Stewart
# another codeEval challenge
# determines whether a sodoku is valid

import sys


def pr9(nums):
	for i in xrange(81):
		if 0 == i%9:
			print ''
		print nums[i],


def missing(nums):
	for i in xrange(1,len(nums)+1):
		if i not in nums:
			return True
	else:
		return False


def isValid4(nums):
	lines = []
	
	for i in xrange(0,16,4):	#appends rows
		lines.append(nums[i:i+4])
	for i in xrange(4):			#appends cols
		lines.append([nums[i],nums[4+i],nums[8+i],nums[12+i]])
	for i in [0,2,8,10]:		#appends boxes
		lines.append([nums[i],nums[i+1],nums[i+4],nums[i+5]])
	
	for line in lines:
		if missing(line):
			return False
	else:
		return True


def isValid9(nums):
	lines = []
	
	for i in xrange(0,81,9):
		lines.append(nums[i:i+9])
	for i in xrange(9):
		a = []
		for j in xrange(0,81,9):
			a.append(nums[i+j])
		lines.append(a)
	for i in [0,3,6,27,30,33,54,57,60]:
		lines.append([nums[i],nums[i+1],nums[i+2],nums[i+9],nums[i+10],nums[i+11],nums[i+18],nums[i+19],nums[i+20]])
	
	for line in lines:
		if missing(line):
			return False
	else:
		return True



def main(args):
	if len(args) != 2:
		print 'Usage ~$ ' + args[0] + ' filename.txt'
		sys.exit(0)
	else:
		filename = args[1]
	
	with open(filename, 'r') as f:
		for line in f:
			N,nums = line.strip().split(';')
			N = int(N)
			nums = [int(x) for x in nums.split(',')]
			
			if N == 4:
				print isValid4(nums)
			elif N == 9:
				print isValid9(nums)


if __name__ == "__main__":
	main(sys.argv)
