# Phillip Stewart
# Converts strings into morse code

import sys

morseD = {'.-':'A',  '-.-.':'C',  '-...':'B',  '.':'E',  '-..':'D',  '--.':'G',  '..-.':'F',  '..':'I',  '....':'H',  '-.-':'K',  '.---':'J',  '--':'M',  '.-..':'L',  '---':'O',  '-.':'N',  '--.-':'Q',  '.--.':'P',  '...':'S',  '.-.':'R',  '..-':'U',  '-':'T',  '.--':'W',  '...-':'V',  '-.--':'Y',  '-..-':'X',  '--..':'Z',  '.----':'1',  '-----':'0',  '...--':'3',  '..---':'2',  '.....':'5',  '....-':'4',  '--...':'7',  '-....':'6',  '----.':'9',  '---..':'8'}

def decode(word):
	w = []
	for letter in word:
		w.append(morseD[letter])
	return ''.join(w)


def main(args):
	if len(args) != 2:
		print 'Usage ~$ ' + args[0] + ' filename.txt'
		sys.exit(0)
	else:
		filename = args[1]
	
	with open(filename, 'r') as f:
		for line in f:
			words = line.strip().split('  ')
			for word in words:
				print decode(word.split()),
			print ''


if __name__ == "__main__":
	main(sys.argv)
