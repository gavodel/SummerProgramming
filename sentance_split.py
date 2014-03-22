#space + lower case
#full stop followed by digit 
#mr.jim
#www.apex.com
#full stop + comma or full stop
in_filename = 'C:\Users\Gavin\Documents\GitHub\SummerProgramming\\sent.txt'
out_filename = 'C:\Users\Gavin\Documents\GitHub\SummerProgramming\\sentout.txt'
fin = open(in_filename,"r")
fout = open(out_filename,"w")
y = fin.read()

newstring=""
for i in range(0, len(y)):
	if y[i] == "." and y[i]+1 == ',' :
		newstring+=y[i]
	elif y[i] =='?'or'!':
		newstring+=y[i]+"\n"
	elif y[i]=='.':
		newstring+=y[i]+"\n"
	else:
		newstring+=y[i]
	
fout.write(newstring)
		
	
fout.close()
fin.close()
