#-*- coding: utf-8 -*-
def translate(english ):
	swede=[]
	u = {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"ar"}
	for i in range(0,len(english)):
		if english[i] in u:
			y = u[english[i]]
		else:
			y = english[i]
		swede.append(y)
	return swede	

h=translate(["merry", "christmas", "and", "happy", "new", "year"])
print h

