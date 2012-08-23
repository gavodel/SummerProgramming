def pangram(a,x):

	for i in range(0,len(x)):
		if not x[i] in a:
			return False	
	return True
			
	
		
	
	
y = pangram("The quick brown fox jumps over the lazy dog",['a', 'b', 'c', 'd', 'e', 'f', 'g' ,'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])

if y:
	print "The sentance is a pangram"
else:
	print "The sentance is not a pangram"
	
	
