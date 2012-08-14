#python -i "$(FULL_CURRENT_PATH)"
def consonant(letter):
	if letter in ['a','e','i','o','u']:
		return False
	else:
		return True 

		
def new(word):
	newstring = ""
	for y in word:
		j=consonant(y)
		if j:
			newstring += y + "o" + y
		
		else:
			newstring += y
		
		
			
		
		
	
	return newstring
		
print new('this is fun')