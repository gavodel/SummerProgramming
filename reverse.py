#python -i "$(FULL_CURRENT_PATH)"
def reverse(word):
	newstring = ""
	for y in word:
		newstring = y + newstring
	return newstring
	

print reverse('I am testing')
