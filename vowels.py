def vowel(letter):
	
	if letter in ['a','e','i','o','u']:
		return True 
	else:
		return False 

		
j = vowel(raw_input(""))
if j:
	print("vowel")
else:
	print("not vowel")