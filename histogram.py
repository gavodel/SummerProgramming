def histogram(n):
	for i in range(0,len(n)):
		j=n[i]
		print generate_n_chars(j,'*')

	
def  generate_n_chars(n,c):
	newstring = ""
	for i in range(0,n):
		newstring += c 
	return newstring
	
