def right_justify(name):
	length = len(name)
	spaces = 70 - length
	newstring = ""
	for i in range(spaces):
		newstring += " "
	newstring += name
	return newstring
#print right_justify(raw_input(" "))	
def max( num1, num2):
	if num1<num2:
		return num1
	if num2<num1:
		return num2
	if num1==num2:
		return num2
def max3( a,b,c):
	big = max(a,b)
	if c>big:
		return c
	else: 
		return big

		
def brainmelt(x, y):
	y = x + y

def hello(name,name2):
	return "hello %s and %s !" %(name, name2)

def word():
	return 'gavin'

print hello(word(),word())
	
