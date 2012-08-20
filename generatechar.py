def  generate_n_chars(n,c):
	newstring = ""
	for i in range(0,n):
		newstring += c 
	return newstring
	
print generate_n_chars(5,'x')