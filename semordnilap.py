def semordnilap(word):
	newstring = ""
	for y in word:
		newstring = y + newstring
		
	if word == newstring:
		return True
	else:
		return False
	
f = open('C:\Users\Gavin\Documents\GitHub\SummerProgramming\semordnilap.txt', 'r')

y = f.readlines()
for i in range(0,len(y)):
	semordnilap(y)
	if y[i]+y[i+1] == True:
		print "%s %s"%(y[i]+y[i]+1)

