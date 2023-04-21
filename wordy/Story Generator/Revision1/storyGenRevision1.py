
###############################################################################
################### Story Generator - Joseph Grimer 2016 ######################
###############################################################################

### Version 5 - Reforming Emotional system
### Version 6 - Gccidentally fixed endless story problem by making emotional
### reactions more random.
# Was originall Version 6'ing for Aesop Fables... Going back to traditional
#story (person not animal based)
### Version 7 - another reformation based on the idea that emotions are only
# memory incoherence notifiers (tetris based best-state emotion system)
## Version 8 - Abandoning curstate emotional tetris... just going for flesh atm
'''
just having fun here... future functionlity
- currently everything in past tense... and conjugations haven't kicked in.
- make story a local object passed around?

Two defining principles of generated narrative interaction:
golden rule: love thy neighbour as thyself?
silver rule??

Version 7 notes:
A balanced reality is one in which people act, and other people react,
and that's it.
the reaction is the completion of the action...? So if the action is a 7,
the reaction should be a 3?? and if the action is a ten, the person dies?
Okay, a big part of an action is the expected reaction. If the expected
reaction is okay, then all is good with the world. If somebody gave me a car
they would expect a big thank you, or a small service, but not expect me to
pay for it. They would expect the same of me as I would of them in the reverse
circumstance.
Perhaps all actions simply need acceptance to be fullfilled?
A question needs an answer... because an answer shows that you accepted the
question by attempting to solve it.
A gift needs a thank you. A person gives a gift because... ? They thing the 
person deserves it? No... They do it for the good of the person?
So a character is all about they care about other characters. The story starts 
when one character is hit by a bowlingBat?

as states of well-being get worse, they branch out more, because there are 
more evils than goods, because evils are imperfections.
so emotional state is 10, physical state is 10, spiritual state is 10, mental 
state is 10
they are all of their own sizes, but like pizzas, things go missing.

fix yourself before fixing others? the holes are bigger than the tools... ? 
repay debts??

love thy neighbour as thyself doesn't neccessarily mean give your neighbour 
as much time as yourself (or vice-versa) but simply help yourself when you 
need helping, and help your neighbour when they need helping.

version 8 notes:

Story elements:
Characters
> (Abilities)
Goal
(Local Situation + Global Situation)
'''

#from vocabulary import * #importa all vocab vars

############################ main functions ###################################


def main():

	print("Welcome to StoryGen... Your Personal Narrative Generator")
	
	promptForSeed()
	
	generatePlot()

#	story.addPeople3(2)
#	story.describePeople()
#
#	alpha=location()
#	alpha.describe()
#	
#	for each in range(0,3):
#		resolvePlot2()

	story.recount()

# move to narrative class
def generatePlot():
	story.state(["A Story about a man [Jim] who's looking for [Enlightenment] \
with [One Leg] in a world of [False Optimism] and a [Broken family]"])

# plot resolver
def resolvePlot():
	settled=False
	for person in story.people:
		if person.feelingNo!=0:
			for otherPerson in story.people:
				if person!=otherPerson:
					person.react(otherPerson)
					break # no need to hasstle everbody, satisfied
			settled=True
	return settled

# plot resolver
def resolvePlot2():
	for person in story.people:
		person.act()

################################### Classes ###################################

class narrative:
	def __init__(self): # (self,name)
		self.title="A Story at a time and in a place"
		self.lines = []
		self.people= []
	def addPeople3(self,number):
		for each in range(0,number):
			newPerson=person3()
			self.people.append(newPerson)
	def describePeople(self):
		for person in self.people:
			person.describe()
	def state(self,ary):
		string=ary[0].capitalize()
		for word in ary[1:]:
			if word != "":
				string+=" " + word
		string+=". \n"
		self.lines.append(string)
	def recount(self):
		print(self.title + "\n---")
		print("".join(self.lines))
	def blankLine(self):
		self.lines.append("\n")

## NOTE: Move this into one of the classes
names=["Jim","Lee","Don","Tee","Long","Shee","Tar","Bon","Dill","Jin","Lin",
"Mon","Noe","Po","Ron","See","Tie","Umm","Vay","Won","Xee","Yo","Zee","Pin",]
class person3:
	def __init__(self): # (self,name)
		self.name=self.getName()
		self.powers=["Read Book"] # natural verbs/abilities
		### emotional state: based on the idea of a tetris puzzle:
	def describe(self):
		# can do this
		story.state([self.name,"esists"])
	def getName(self): # doesn't work if you use up everybody!
		global names
		randomNameNo = oneIn(len(names))
		randomName = names[randomNameNo]
		del names[randomNameNo] #removing so we don't get repeats in story
		return randomName
	def act(self):
		# help oneself
		for aspect in self.state:
			if aspect[1]<0:
				story.state([self.name,"gets",aspect[0]])
				aspect[1]= -aspect[1]
				return
		# else: do random things to others...
		for otherPerson in story.people:
			if otherPerson!=self:
				story.state([self.name,oneOf(["smiles at","yells at","teaches",
				"learns from","attacks"]),otherPerson.name])
				return
		# examine self - if: act
		# examine neighbour - if: act
		# else ???
		story.blankLine()

placeNames=["Clindar","Bawn","Chette","Doon","Efier","Forg","Goan"]
placeDescriptions=[["red","blue","green"],["tower","town","village","house"]]
class location:
	def __init__(self): # (self,name)
		self.name=self.getName()
		self.powers=[] # natural verbs/abilities
		self.state=[["home",2],["family",4],["friend",-4]] # 8 out of 10.
	def describe(self):
#		for each in self.normalEmotion
		description=[self.name,"is"]
		for each in placeDescriptions:
			description.append(oneOf(each))
		story.state(description)
	def getName(self): # doesn't work if you use up everybody!
		global placeNames
		randomNameNo = oneIn(len(placeNames))
		randomName = placeNames[randomNameNo]
		del placeNames[randomNameNo] #removing so we don't get repeats in story
		return randomName

############################ Other Functions ##################################
################## Grammar and Spelling Related Functions ##################### 

def aOrAn(words): # still need to fix spaces problem
#	print(words)
	for word in words:
		if word=="":
			continue
		elif word[0].lower() in ["a","e","i","o","u"]:
			return "an " + " ".join(words)
		else:
			return "a " + " ".join(words)

############################### Randomisers ###################################

seeds = [] # string based randomiser setup
lastSeed = -1

def promptForSeed():

	print("Please input your chosen narrative seed")
	seedStr = raw_input("> ") # this is a random sit on the keyboard string
	global seeds
	global lastSeed

#	#failsafe
	if seedStr == "":
	    seedStr = "s?3jo;nw#mu[zla[4235%46%34^&57+=6"

	#prepare randomiser
	for char in seedStr:
		seeds.append(ord(char))

def aSeed():
	global seeds
	global lastSeed
	lastSeed += 1
	if lastSeed >= len(seeds):
		lastSeed = 0
	seeds[lastSeed]+=59
	return seeds[lastSeed]

def oneOf(ary,prob=1): # uses aSeed, and returns a no
	if aSeed()%prob == 0:
		return ary[aSeed()%(len(ary)-1)]
	else:
		return ""

def oneIn(max):
	return ((aSeed()+aSeed()+aSeed()+aSeed()+aSeed())%max) # 400-800?

############################ Global Variables: ################################

personElements=[ #tetris #need vs have?



]


### run main

story = narrative()

main()

############################# Old Functions ###################################



