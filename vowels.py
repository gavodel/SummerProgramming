def vowel(letter):
	i=letter
	if i in ['a','e','i','o','u']:
		return True 
	else:
		return False 

		
j = vowel(raw_input(""))
if j ==True:
	print("vowel")
else:
	print("not vowel")