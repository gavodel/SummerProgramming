import random
def guess_the_anagram():
	i = random.choice(['gavin','richard','kelly','ian', 'rosie'])
	
	name = i.split(" ")
	anstring = ""
	for j in name:
		mix=random.choice(name)
		anstring +=mix
	print "anagram = %s"%anstring
	
guess_the_anagram()