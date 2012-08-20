from maxinlist import max_in_list
from histogram import histogram
from summutli import sum, multiply


def wordlen(words):
	lengths=[]
	for i in range(0,len(words)):
		y = words[i]
		j = len(y)
		lengths.append(j)
	return lengths
	
wordlengths = wordlen(["bird", "python", "penguin", "linuxfjsdhsgdhoahgdoh"])
print max_in_list(wordlengths)
histogram(wordlengths)
print sum(wordlengths)
print multiply(wordlengths)

# [4, 6, 7, 5]