def is_member(x,a):
	for i in a:
		if i == x:
			return True
		else:
			return False
	

x='g'
a='gavin'
y = is_member(x,a)

if y:
	print "%s is in the word %s"%(x,a)
else:
	print "%s is not in the word %s"%(x,a)