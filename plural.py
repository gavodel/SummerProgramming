def make_3sg_form(word):
	lastletter=word[len(word)-1]
	last2letter=word[len(word)-2:len(word)]
	if lastletter =='y':
		plural = word[0:len(word)-1]
		plural += 'ies'
	elif lastletter in ['o', 'x', 'z']:
		plural = word
		plural += 'es'
	elif last2letter in ['ch','sh']:
		plural = word
		plural += 'es'
	else:
		plural = word
		plural += 's'
	return plural



print make_3sg_form("brush")
print make_3sg_form("run")
print make_3sg_form("try")
print make_3sg_form("fix")

#y = ies
# o, ch, s, sh, x or z = es
# s
