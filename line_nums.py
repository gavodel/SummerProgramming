
	

in_filename = 'C:\Users\Gavin\Documents\GitHub\SummerProgramming\\numbers.txt'
out_filename = 'C:\Users\Gavin\Documents\GitHub\SummerProgramming\\numbers_out.txt'
fin = open(in_filename, "r")
fout = open(out_filename, 'w')
lines = fin.readlines()
#["first\n", "second\n"]

for i in range(0, len(lines)):
	line = lines[i]
	output_string = "%d %s" % (i, line)
	
	fout.write(output_string)
fout.close()
fin.close()