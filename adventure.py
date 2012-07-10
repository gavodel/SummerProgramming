#python -i "$(FULL_CURRENT_PATH)"


def lor():
	users_input = raw_input("left or right?")
	print "\n"
	while users_input not in ['left','right']:
		print "INVALID CHOICE"
		print "\n"
		users_input = raw_input("left or right?")
		print "\n"
	if users_input == 'left':
		return True
	elif users_input == 'right':
		return False
def option():
	users_input = raw_input("y or n?")
	print "\n"
	while users_input not in ['y','n']:
		print "INVALID CHOICE"
		print "\n"
		users_input = raw_input("y or n?")
		print "\n"
	if users_input == 'y':
		return True
	elif users_input == 'n':
		return False
def start():
	raw_input("") 	
	print "WELCOME TO MY ADVENTURE \n \nThe objective is to make it through the forest"
	raw_input("")
	print "Do you want to enter the forest?"
	y = option()
	if y:
		bear()
	else:
		return None
def bear():
	print"Do you want to go along the path or turn into the trees?\n\nIf path..type y \nIf tress...type n"

	y=option()

	if y == True:
		print "Nice and safe..bit muddy though"
		raw_input("")
		house()
	else:
		print "BEAR!!"
		raw_input("")
		print "It rips you apart"
		raw_input("")
		return None
def house():
	print "Theres a house..looks haunted though\n\nWant to go in?"
	
	y=option()
	if y == True:
		print "The door opens by itself...Want to enter?"
		monster()
	else:
		print "The road looks dark but at least theres no ghosts or witchs"	
		raw_input("")
		wow()
def wow():
	print"You hear howling in the distance..could be the wind..might also be wolves"
	raw_input("")
	print "Do you want to go left....towards the howling\nOr right.....away from the howling"
	left = lor()
	if left == True:
		wolf()
	else:
	 
		exit()
def wolf():
	print "It wasnt the wind..a herd of wolves surround you and are growling madley"
	raw_input("")
	print"A man appears with a shotgun and blows the wolves to bits\nHe wants you to follow him to his house\nDo yo follow him"
	man()
def man():
	y = option()
	if y == True:
		print "He's a cannabil and he eats you!!"
		raw_input("")
		end()
		raw_input("")
		return None
	else:
		print "Good choice he looked a bit scarey"	
		exit()
def exit():
	print"There seems to be a an shortcut through hedge to the end of the forest\nThe normal exit is a mile to the left"
	raw_input("")
	print "Want to take the shortcut?"
	congrat()
		
def congrat():
	y=option()
	if y == True:
		print "eaten by a man-eating squirrel!!!"
		raw_input("")
		print "shouldn't have gone the shortcut!!"
		raw_input("")
		end()
		return None
	else:
		print "A bit longer but you made it!!"
		raw_input("")
		print"Congratulations you made it through the forest"
		raw_input("")
		print"Well done"
		return None
def monster():
	y=option()
	if y == True:
		print "You get eaten by a monster!!!"
		return None
	else:
		print "Good choice..looks a bit scary....back to the road!!"
		raw_input("")
		wow()
def end():	
	print "Hard luck!!"
	raw_input("")
	print "Bye!!"
	raw_input("")
	
start()
	