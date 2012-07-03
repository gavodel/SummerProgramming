#python -i "$(FULL_CURRENT_PATH)"
import random
def mix(yes ,no):
	i = random.randint(yes,no)  
	return i

def peno(player_name):
	i = mix(1,3)
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
		
	if users_input in ['l', 'r', 'c']:
		if i == 1 or i==3:
			print "And he scores"
			score=True
		else: 
			print"And he misses"
		print "\n"
		raw_input("")
		return score
	
def print_team(team_name, team):
	print team_name
	
team1 = ['Keith Baker','Gavin Delaney','Grant Baker','Luke Foley','Ben Foley']
team2 = ['Kate Foley','Kelly Delaney','Rosie Delaney','Gwyneth Baker','Granny']
raw_input("")	
print "\n"	

print_team("Ireland", team1)
for i in range(0, 5):
	print "%s "%team1[i]
raw_input("")

print_team("England", team2)
for i in range(0, 5):
	print "%s "%team2[i]


print "\n"
score1=0
score2=0
raw_input("")

for i in range(0, 5):
	scored1 = peno("[Ireland] %s "%team1[i])
	print "\n"
	scored2 = peno("[England] %s "%team2[i])
	if(scored1 == True):
		score1+=1
	if(scored2 == True):
		score2+=1
	print("%d-%d\n"%(score1,score2))
	raw_input("")
	print "\n"
	
if score1>score2:
	print("Ireland win!!!")
elif score2>score1:
	print("England win!!!")
elif score1==score2:
	print("Its a draw...sorry havent made sudden death yet!!")

print("%d-%d"%(score1,score2))