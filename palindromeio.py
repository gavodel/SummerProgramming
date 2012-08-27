from palindrome import palindrome


f = open('C:\Users\Gavin\Documents\GitHub\SummerProgramming\pal.txt', 'r')

y = f.readlines()
for i in range(0,len(y)):
	y[i] = y[i].strip()
	h = palindrome(y[i])
	
	if h:
		print '%s............is a palindrome\n'% y[i]
	else:
		print '%s............is not palindrome\n'% y[i]
	