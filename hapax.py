from hapaxfreq import char_freq

f = open('C:\Users\Gavin\Documents\GitHub\SummerProgramming\\alice.txt',
	'r')

y = f.read()

char_freq(y)

f.close()