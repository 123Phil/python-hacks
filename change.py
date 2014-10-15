# Phillip Stewart
# from one of the codeEval challenges

import sys

def makeChange(cents):
	coins = []
	while cents - 10000 >= 0:
		cents -= 10000
		coins.append('ONE HUNDRED')
	while cents - 5000 >= 0:
		cents -= 5000
		coins.append('FIFTY')
	while cents - 2000 >= 0:
		cents -= 2000
		coins.append('TWENTY')
	while cents - 1000 >= 0:
		cents -= 1000
		coins.append('TEN')
	while cents - 500 >= 0:
		cents -= 500
		coins.append('FIVE')
	while cents - 200 >= 0:
		cents -= 200
		coins.append('TWO')
	while cents - 100 >= 0:
		cents -= 100
		coins.append('ONE')
	while cents - 50 >= 0:
		cents -= 50
		coins.append('HALF DOLLAR')
	while cents - 25 >= 0:
		cents -= 25
		coins.append('QUARTER')
	while cents - 10 >= 0:
		cents -= 10
		coins.append('DIME')
	while cents - 5 >= 0:
		cents -= 5
		coins.append('NICKEL')
	while cents - 1 >= 0:
		cents -= 1
		coins.append('PENNY')
	
	print ','.join(coins)
	
	



def main(args):
	if len(args) != 2:
		print 'Usage ...'
		sys.exit(0)
	else:
		filename = args[1]
	
	
	with open(filename, 'r') as f:
		for line in f:
			cost,paid = line.strip().split(';')
			if '.' in cost:
				a,b = cost.split('.')
				cost = int(a)*100 + int(b)
			else:
				cost = int(cost)*100
			if '.' in paid:
				a,b = paid.split('.')
				paid = int(a)*100 + int(b)
			else:
				paid = int(paid)*100
			
			change = paid - cost
			
			if change < 0:
				print 'ERROR'
			elif change == 0:
				print 'ZERO'
			else:
				makeChange(change)
	
	


if __name__ == "__main__":
	main(sys.argv)
