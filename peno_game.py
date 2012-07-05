#python -i "$(FULL_CURRENT_PATH)"
import random


def peno(player_name):
	i = random.choice(['l', 'r', 'c','saved'])
	score = False
	print "%s steps up" % player_name
	print "\n"
	users_input = raw_input("If you want to shoot left type, l\nIf you want to shoot right type, r\nIf you want to shoot down the center type, c \ntype here: ")
	print "\n"
	while users_input not in ['l', 'r', 'c']:
		print "INVALID CHOICE"
		print "\n"
		users_input = raw_input("If you want to shoot left type, l,\nIf you want to shoot right type, r,\nIf you want to shoot down the center type, c \ntype here: ")
		print "\n"
		
	if i=='saved':
		print "And the goalie saves it"
	elif not i == users_input:
		print "And he scores"
		score=True
	else: 
		print"And he misses" 
	print "\n"
	raw_input("")
	return score
	
def print_team(team_name, team):
	print team_name
	for i in range(0, 5):
		print "%s "%team[i]
	raw_input("")

print "PENALTY GAME"
team1 = ['Wayne Rooney','Ashley Young','Nani','Javier Hernadez','Ryan Giggs']
team2 = ['Xavi Hernandez','Lionel Messi','Andres Iniesta','Cesc Fabregas','David Villa']
raw_input("")	
print "\n"	

print_team("MAN UNITED", team1)
print_team("BARCELONA", team2)


print "\n"
score1=0
score2=0
raw_input("")


for i in range(0, 5):
	scored1 = peno("[MAN UNITED] %s "%team1[i])
	print "\n"
	scored2 = peno("[BARCELONA] %s "%team2[i])
	if(scored1 == True):
		score1+=1
	if(scored2 == True):
		score2+=1
	print("%d-%d\n"%(score1,score2))
	raw_input("")
	print "\n"
	 
	
	if (score1-score2)>(4-i):
		break
	elif (score2-score1)>(4-i):
		break

if score1==score2:
	print("SUDDEN DEATH!!!")
	print("\n")
	i = 0
	while score1 == score2:
		scored1 = peno("[MAN UNITED] %s "%team1[i])
		print "\n"
		scored2 = peno("[BARCELONA] %s "%team2[i])
		if(scored1 == True):
			score1+=1
		if(scored2 == True):
			score2+=1
		print("%d-%d\n"%(score1,score2))
		raw_input("")
		print "\n"
		i+=1
		if i == 5:
			i = 0

if score1>score2:
	print("Man United win!!!")
elif score2>score1:
	print("Barcelona win!!!")


print("%d-%d"%(score1,score2))