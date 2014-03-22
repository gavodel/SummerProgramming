in_filename = 'C:\Users\Gavin\Documents\GitHub\SummerProgramming\\anagramio.txt'

fin = open(in_filename, "r")

def anagram(word1, word2):
	if not len(word1) == len(word2):
		return False
		
	for letter in word1:
		if not letter in word2:
			return False
	return True
words = fin.readlines()
results = {}
for word_n in words:
	#word = word_n.strip()
	#found = False
	#for key in results.keys():
	#	if anagram(word, key):
	#		results[key] += 1
	#		found = True
	#		break
	#if not found:
	#	results[word] = 0 	
	
	word = word_n.strip()
	results[word] =0
	for i_n in words:
		i= i_n.strip()
		if not word == i:
			y = anagram(word,i)
			if y:
				results[word] += 1

				

print results


#y = angram("acute", "cutea")
#if y:
#	print"anagram"
#else:
#	print"not"