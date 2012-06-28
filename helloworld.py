#python -i "$(FULL_CURRENT_PATH)"
import random
def mix(yes ,no):
	i = random.randint(yes,no)  
	return i

def peno(player_name):
	i = mix(1,3)
	score = False
	print "%s steps up" % player_name
	raw_input("")
	if i == 1 or i==3:
		print "And he scores"
		score=True
	else: 
		print"And he misses"
	print "\n"
	raw_input("")
	return score


raw_input("")	
print "\n"	
print "Ireland"	
for j in range(1, 6):
	print "Player %d "%j
raw_input("")
print "\nEngland"
for j in range(6, 11):
	print "Player %d"%j
print "\n"
score1=0
score2=0
raw_input("")
for j in range(1, 6):
	scored1 = peno("[Ireland] Player %d"%j)
	print "\n"
	scored2 = peno("[England] Player %d"%(j+5))
	if(scored1 == True):
		score1+=1
	if(scored2 == True):
		score2+=1
	print("%d-%d\n"%(score1,score2))
	print "\n"
	
if score1>score2:
	print("Ireland win!!!")
elif score2>score1:
	print("England win!!!")
elif score1=score2:
	print("Its a draw...sorry havent made sudden death yet!!")

print("%d-%d"%(score1,score2))