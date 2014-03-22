import random
f = open('C:\Users\Gavin\Documents\GitHub\SummerProgramming\\lingo.txt', "r")
def lingo(word,guess):
	newstring= ""
	if not len(word) == len(guess):
		print "The word you have guessed is the wrong length ,you idiot"
		return False
	for i in range(0,len(word)):
		letter = word[i]
		guessletter = guess[i]
		if guessletter in word and guessletter==letter:
			newstring+="[%s]"%guessletter
		elif guessletter in word and not guessletter==letter:
			newstring+="(%s)"%guessletter
		else:
			newstring+=guessletter
	print newstring
	if guess == word:
		return True
	else:
		return False

words = f.readlines()
word_n = random.choice(words)

word = word_n.strip()
print "I've thought of a word\nIt is %d letters long\nCan u guess what it is?"%len(word)	
guess = raw_input("")
finished = lingo(word,guess)	

while not finished:
	print "Guess again"
	guess = raw_input("")
	finished = lingo("snake",guess)
raw_input("")
print "You win"	
	
			