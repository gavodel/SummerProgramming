from vowels import vowel


def make_ing_form(word):
	lastletter=word[len(word)-1]
	last2letter=word[len(word)-2:len(word)]
	last3letter=word[len(word)-3:len(word)]
	
	if not vowel(last3letter[0]):
		if vowel(last3letter[1]):
			if not vowel(last3letter[2]):
				add = word[0:len(word)-1]
				add = add + last3letter[2]*2 + 'ing'
	elif last2letter =='ie':
		add = word[0:len(word)-2]
		add += 'ying'
	elif word in ['be', 'see', 'flee', 'knee']:
		add = word
		add += 'ing'
	elif lastletter =='e':
		add = word[0:len(word)-1]
		add += 'ing'	
	else:
		add = word
		add += 'ing'
	return add



print make_ing_form("lie")
print make_ing_form("see")
print make_ing_form("move")
print make_ing_form("hug")
#e = ing
#ie = y + ing
#c-v-c = double + ing
# ing
