#python -i "$(FULL_CURRENT_PATH)"
def palindrome(word):
	newstring = word[::-1]
	if word == newstring:
		return True
	else:
		return False

y = palindrome('radar')

if y:
	print "palindrome"
else:
	print "not palindrome"

	