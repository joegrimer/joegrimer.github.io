# RPG - Joseph Grimer - 15 Jul 2016 - 21 Nov 2016
# simple RPG - based on a story I half wrote once

#import re # regexp library?
#from rand import radiant # radiant(1,10)

currentState = [12] # HP
quitStrings = ["exit","quit","die","bye"]
places = []
#locs = locations #shorthand
here=[]

def main():

	initiate()
	wanWorld()
	goToPlace("alpha")
	showHere()
	
	#thye loop
	while True:
		response = raw_input(">").lower().strip()
		words = response.split(" ")

		if response in quitStrings:
			print "Goodbye"
			break
		else:
			print "What did you say?"

def initiate():
	print "Hello... Welcome to the Land of Key."
	print "You have " + str(currentState[0]) + " Hit Points"
	print "You rise to the surface... you are Wan... initiated onto the surface of Key. The green sky beneath you only altereed by the smaller lighter shade."

def wanWorld():
	newPlace("alpha","Green Sky... dark metallic-lined surface floating above you.",[],["echo"])
	newPlace("echo","This place is different.",["An arm"],["alpha"])
	
#end of wanWorld

def newPlace(name,description,contents,near):
	global places
	places.append([name,description,contents,near])

def goToPlace(name):
	global places
	global here
	for location in places:
		if name==location[0]:
#			print("we have a match on "+name)
			here = location

def showHere():
	print("You are located in: "+here[0])
	print("Description: "+here[1])
	print("Can go to: "+here[3][0])


#Run Main:
if __name__ == '__main__':
	main()
	

