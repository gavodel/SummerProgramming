#python -i "$(FULL_CURRENT_PATH)"


def answer():
	aq=False
	bq=False
	cq=False
	dq=False
	users_input = raw_input("A, B, C or D?")
	print "\n"
	while users_input not in ['a', 'b', 'c','d']:
		print "INVALID CHOICE"
		print "\n"
		users_input = raw_input("A, B, C or D?")
		print "\n"
		
	if users_input =='a' or 'A':
		aq = True
		return aq
	elif users_input =='b' or 'B':
		return bq = True
	elif users_input =='c' or 'C':
		return cq = True
	elif users_input =='d' or 'D':
		return dq = True

def get_questions():
	f = open("qa.txt", "r")
	f.read()
		
def main():
	print "WELCOME TO MY QUIZ\n\nThere are 15 questions\n\nEach question is worth €1,000"
	raw_input("")
	
main()