def correct(sentence):
	newstring = ""
	space_set = False
	for letter in sentence:
	   if letter != " ":
			newstring+=letter
			space_set=False
	   elif letter == " " and space_set == False:
			newstring+=letter
			space_set = True
	return newstring

print correct("This   is  very funny  and    cool.Indeed!")