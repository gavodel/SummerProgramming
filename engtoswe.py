def translate(english ):
	swede=[]
	u= {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"�r"}
	for i in english:
		y = u[english[i]]
		swede.append(y)
	return swede	

h=translate("merry", "christmas", "and", "happy", "new", "year")
print h

