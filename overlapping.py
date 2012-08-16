def overlapping(a,b):
	for i in a:
		for j in b:
			if i == j:
				return True
			
	return False

y=overlapping('vain','great')
	
if y:
	print "overlapping letters"
else:
	print "no overlapping letters"