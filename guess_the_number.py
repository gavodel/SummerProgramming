import random
def guess_the_number():
	i = random.choice([1, 2, 3,4,5,6,7,8,9,10,11, 12, 13,14,15,16,17,18,19,20])
	print i
	users_input = raw_input("Hello! What is your name?\n")
	print "Well, %s, I am thinking of a number between 1 and 20."%users_input
	users_input2_string = raw_input("Take a guess.\n")
	users_input2 = int(users_input2_string)
	sum = 1
	while not i == users_input2:
		if i > users_input2 :
			print "Your guess is too low\n"
			sum+=1
			
		elif i < users_input2:
			print "Your guess is too high\n"
			sum+=1
		print i	
		users_input2 = raw_input("Take a guess.\n")
		
			
	print "Good job, %s! You guessed my number in %d guesses!"%(users_input, sum)







guess_the_number()