
###############################################################################
#################### Story Generator - Joseph Grimer 2016 #####################
###############################################################################

### Version 5 - Reforming Emotional system
'''

just having fun here... future functionlity
- currently everything in past tense... and conjugations haven't kicked in.
- make story a local object passed around?

Two defining principles of generated narrative interaction:
golden rule: love thy neighbour as thyself?
silver rule??
'''

#from vocabulary import * #importa all vocab vars

############################ main functions ###################################


def main():

	print("Welcome to StoryGen... Your Personal Narrative Generator")
	
	promptForSeed()

#	emotionDrivenNarrative3()
	goldenRuleNarrative4()
	story.recount()

# golden rule as in charity
def goldenRuleNarrative4():

	story.addPeople2(2) #flawed
	story.describePeople()
	
	story.blankLine()
	
	for x in range(1,3):
		if resolvePlot2() == False: #story.
			break
		story.state(["looped"])
	
	story.blankLine()
	story.state(["Epilogue:"])
	story.blankLine()
	
	for each in story.people:
		each.feel()

def emotionDrivenNarrative3():

	story.addPeople(2)
	story.describePeople()
	
	story.blankLine()
	
#	narrative begins:
	story.people[0].actOn(story.people[1])
	story.people[1].feel()
	story.people[1].actOn(story.people[0])
	story.people[0].feel()

	story.blankLine() # note: alpha is not affected (yet)

	for x in range(1,3):
		if resolvePlot() == False: #story.
			break
		story.state(["looped"])
	
	story.blankLine()
	story.state(["Epilogue:"])
	story.blankLine()
	
	for each in story.people:
		each.feel()

# plot resolver
def resolvePlot2():
	settled=False
	for person in story.people:
		if person.feelingNo2!=0:
			for otherPerson in story.people:
				if person!=otherPerson:
					person.react(otherPerson)
					break # no need to hasstle everbody, satisfied
			settled=True
	return settled

# plot resolver
def resolvePlot():
	settled=False
	for person in story.people:
		if person.feelingNo2!=0:
			for otherPerson in story.people:
				if person!=otherPerson:
					person.react(otherPerson)
					break # no need to hasstle everbody, satisfied
			settled=True
	return settled


################################### Classes ###################################

class narrative:
	def __init__(self): # (self,name)
		self.title="A story of Woe"
		self.lines = []
		self.people= []
	def addPeople(self,ary):
#		for each in ary:
		self.people.extend(ary)
#			each=person() #declare them in here??
	def addPeople2(self,number=1):
		for each in range(0,number):
			newPerson=person()
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

#		self.title=oneOf(["builder","assasin","juggler","programmer","musician","tailor","seamstress","cook","salesman"])
class profession: # template:Assassin
	def __init__(self): # (self,name)
		job=oneOf(professions)
		self.title=job[0]
#		print(self.title)
		self.description="unfinished"
		self.powers=job[1] # articial verbs/abilities
#		print(self.powers)
		self.feelingNo=0
	def describe(self):
#		print "aoranisReturning>"+aOrAn(self.title)
		story.state([self.title,self.description])


## NOTE: Move this into one of the classes
names=["Jim","Karl","Pharaoah","Queenie","Marty","Doctor Brown","Empressette","Proffessor Plum","Beefy","Bobert","Maxwell","Denvod","Clix","Amias the Third","Bobiatas"]
def getName(): # fairly ### doesn't work if you use everybody!
#	forenames=["Jon","Jim","Karl"] ### add this functionality later
	global names
	randomNameNo = oneIn(len(names))
	randomName = names[randomNameNo]
	del names[randomNameNo] #removing element from list so we don't get repeats in the narrative
	return randomName

def getFeelingCode(): # introvert or extravert
	return (oneIn(5)) #negative is introvert... positive is extravert
	
class person:
	def __init__(self): # (self,name)
		self.name=getName()
		self.powers=humanNaturalPowers # natural verbs/abilities
		self.job=profession()
#		self.powers.extend(self.job.powers) # TEMPORARY: DISABLED JOBS
		self.title=self.job.title
		self.feelingNo=0
		self.feelingNo2=0
		self.feelingCode=getFeelingCode()
		#self.selfControl??
		
	def describe(self):
		story.state([self.name,"was",aOrAn([self.title])])
	def actOn(self,other): #forceActOn
		actionMatch={-2:"shouted at",-1:"threw a mug at",0:"is fine",1:"made a tea for",2:"sang aloud to"}
		actionNo = oneIn(5)-2
		story.state([self.name,actionMatch[actionNo],other.name])
		other.feelingNo2 += actionNo
	def react(self,other): #The new ActOn function
#		self.feel()
#		self.actOn(other)

		actionMatch={-2:"shouted at",-1:"threw a mug at",0:"is fine",1:"made a tea for",2:"sang aloud to"}
		story.state([self.name,actionMatch[self.feelingNo2],other.name])
		other.feelingNo2 = self.feelingNo2 #back to normal!
		self.feelingNo2 = 0 #back to normal!
		other.feel()
	def feel(self): #force to feel
		emotionMatch={-2:"unhappy",-1:"irritated",0:"fine",1:"chuffed",2:"happy"}
		story.state([self.name,"felt",emotionMatch[self.feelingNo2]])

############################ other functions ##################################



################ grammar and spelling related functions ########### 

def aOrAn(words): # still need to fix spaces problem
#	print(words)
	for word in words:
		if word=="":
			continue
		elif word[0].lower() in ["a","e","i","o","u"]:
			return "an " + " ".join(words)
		else:
			return "a " + " ".join(words)

############################### randomisers ###################################

seeds = [] # string based randomiser setup
lastSeed = -1

def promptForSeed():

	print("Please input your chosen narrative seed")
	seedStr = raw_input("> ") # this is a random sit on the keyboard string
	global seeds
	global lastSeed

#	#failsafe
	if seedStr == "":
	    seedStr = "sjonwmuzla[423534634576"

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

humanNaturalPowers=[
#["saved",+5],
#["inspired",+4],
##["listened to",+3],
#["read a narrative to",+3],
#["complemented",+2],
#["sympathised with",+2],
##["played a game with",+2],
["greeted",+1],
["surprised",+1],
["smiled at",+1],
["wished well",+1],
["waved to",+1],
["looked at",+1],
["looked past",-1],
["turned away from",-1],
["ignored",-1],
["said goodbye to",-1],
["scared",-1],
["frowned at",-1],
#["didn't sympathise with",-2],
#["insulted",-2],
#["shouted at",-3],
#["stood on",-4],
#["captured",-5]
##["murdered",-100], ## DISABLED... Causing too many killings!
]
#["",],

#		self.title=oneOf(["builder","assasin","juggler","programmer","musician","tailor","seamstress","cook","salesman"])
professions=[
[ "assasin",[["shot at",-6],["shot",-100],["threatened",-4],["aimed at",0],["fell in love with",+12]] ],
[ "cook",[["baked a cake for",+3],["made a tea for",+1],["made a coffee for",+2],["made dinner for",+2]] ],
[ "fairy",[["blessed",+3],["gave fairy dust to",+6],["appeared to",+1],["cursed",-4]] ],
[ "woodcutter",[["grunted at",+1],["burped at",-2],["threw an axe at",-2],["tried to chop",-4],["gave a tree to",+2]] ],
[ "loner",[["cried to",-3],["gave a flower to",+4],["stole from",-3],["slept near",-3],["begged",-1],["played music to",+1]] ],
#[ "",[["",+],["",+],["",+],["",+],["",+],["",+],["",+],["",+],["",+]]],
#[ "builder",[["",+],["",+],["",+],["",+],["",+],["",+],["",+],["",+],["",+]] ],
[ "orphan",[["asked paternal advice from",-2],["glared at",-2],["hugged",+4],["felt for",0]] ]
]

### run main

story = narrative()

main()

############################ old functions ####################################
'''
Proud of this one, I was... only lasted about 10 hours!
def developnarrative(people): #ary
	unsettled=False
	for person in people:
		if person.feelingNo!=0 and person.feelingNo>=-12: #if a person is normal and not (emotionally) dead
#			story.state([str(person.feelingNo),"should be not zero and higher than -13"])
			for otherPerson in people:
				### possible addition to below: person.feelingNo!=0
				if otherPerson.feelingNo>=-12 and person!=otherPerson:## i.e. if person is alive and not me
#					story.state(["otherPersonFeels",str(otherPerson.feelingNo<-12)])
					person.actOn(otherPerson)
					otherPerson.feel()
					break # I've made somebody feel... no need to make the whole world go bonkers!
			unsettled=True
	return unsettled


'''


