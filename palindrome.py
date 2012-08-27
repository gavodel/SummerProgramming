#python -i "$(FULL_CURRENT_PATH)"
def palindrome(xword):
	word = xword.lower().replace(" ",'')
	newstring = ""
	for y in word:
		newstring = y + newstring
		
	if word == newstring:
		return True
	else:
		return False
	


	