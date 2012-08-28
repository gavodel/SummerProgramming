def char_freq(word):
	u = {}
	for i in range(0,len(word)):
		key = word[i]
		if not key in u:
			u[key] =  1
		else:
			u[key] = u[key] + 1
	for k, v in u.iteritems():
		if v==1:
			print k,v
		