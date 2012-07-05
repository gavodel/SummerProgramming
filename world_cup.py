#python -i "$(FULL_CURRENT_PATH)"
import random


def match1(team1,team2):
	items=[1, 2, 3, 4, 5, 6, 0]
	items2=[1, 2, 3, 4, 5, 6, 0]
	win1=False
	i = random.choice(items)
	j = random.choice(items2)
	print "%s vs %s"%(team1,team2)
	raw_input("")
	print "%d - %d"%(i,j)
	raw_input("")
	if i < j:
		print "%s win" %team2
		win1 = True
	elif i>j:
		print  "%s win" %team1
	elif i == j:
		print "draw"
	return win1

def match2(team3,team4):
	items=[1, 2, 3, 4, 5, 6, 0]
	items2=[1, 2, 3, 4, 5, 6, 0]
	i = random.choice(items)
	j = random.choice(items2)
	win2=False
	print "%s vs %s"%(team3,team4)
	raw_input("")
	print "%d - %d"%(i,j)
	raw_input("")
	if i < j:
		print "%s win" %team4
		win2=True
	elif i>j:
		print  "%s win" %team3
	elif i == j:
		print "draw"
	return win2

team = ['Spain','Ireland','France','Germany']

raw_input("")
w1 = match1(team[0],team[1])
raw_input("")
w2 = match2(team[2],team[3])
raw_input("")
if w1 == True and w2 == True:
	match1(team[1],team[3])
elif w1 == True and w2 == False:
	match1(team[1],team[2])
elif w1 == False and w2 == True:
	match1(team[0],team[3])
elif w1 == False and w2 == False:
	match1(team[0],team[2])
	





