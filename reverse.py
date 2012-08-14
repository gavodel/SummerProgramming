#python -i "$(FULL_CURRENT_PATH)"
def reverse(word):
	newstring = word[::-1]
	return newstring
	

print reverse('I am testing')
