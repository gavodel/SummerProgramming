def overlapping(a,b):
	for i in a:
		for j in b:
			if i == j:
				return True
			else:
				return False

y=overlapping('gavin','great')
	
if y:
	print "overlapping letters"
else:
	print "no overlapping letters"