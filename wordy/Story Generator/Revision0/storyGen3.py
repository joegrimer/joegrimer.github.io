
############################################################################
################## Story Generator - Joseph Grimer 2016 ####################
############################################################################

'''

just having fun here... future functionlity
- currently everything in past tense... and conjugations haven't kicked in.
- make tale a local object passed around?

Two defining principles of generated story interaction:
golden rule: love thy neighbour as thyself?
silver rule??
'''

#from vocabulary import * #importa all vocab vars

### main functions


def main():

	print("Welcome to StoryGen... Please input your chosen story number randomiser")
	seedStr = raw_input("> ") # this is a random sit on the keyboard string
	global seeds
	global lastSeed

#	#failsafe
	if seedStr == "":
	    seedStr = "sjonwmuzla[423534634576"

	#prepare randomiser
	for char in seedStr:
		seeds.append(ord(char))

#	print(getName())
	emotionDrivenStory3()
	tale.recount()


def emotionDrivenStory3():

#	initiation
	protagonist=person()
	antagonist=person()
	alpha=person()
	tale.addPeople([protagonist,antagonist,alpha])
	protagonist.describe()
	antagonist.describe()
	alpha.describe()
	
	tale.blank()
	
#	story begins:
	antagonist.actOn(protagonist)
	protagonist.feel()
	protagonist.actOn(antagonist)
	antagonist.feel()
	alpha.actOn(alpha) # he starts his own problems :)
	alpha.feel()
	tale.blank() # note: alpha is not affected (yet)

	for i in range(1,20):
		if developStory(tale.people) == False: # ergo: if the story didn't develop
			tale.state(["-------The Natural End of the Story-------"])
			break
		tale.blank()
	
	tale.state(["---------- Epilogue:"])
	protagonist.feel()
	antagonist.feel()
	alpha.feel()


def developStory(people): #ary
	unsettled=False
	for person in people:
		if person.feelingNo!=0 and person.feelingNo>=-12: #if a person is normal or (emotionally) dead
			for otherPerson in people:
				if otherPerson.feelingNo>-12 and person!=otherPerson:## i.e. if person is alive and not me
#					tale.state(["otherPersonFeels",str(otherPerson.feelingNo<-12)])
					person.actOn(otherPerson)
					otherPerson.feel()
					break # I've made somebody feel... no need to make the whole world go bonkers!
			unsettled=True
	return unsettled

################################### Classes ############################################

class story:
	def __init__(self): # (self,name)
		self.title="A Tale of Woe"
		self.lines = []
		self.people= []
	def addPeople(self,ary):
#		for each in ary:
		self.people.extend(ary)
#			each=person() #declare them in here??
			
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
	def blank(self):
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
		tale.state([self.title,self.description])

class person:
	def __init__(self): # (self,name)
		self.name=getName()
		self.powers=humanNaturalPowers # natural verbs/abilities
		self.job=profession()
#		self.powers.extend(self.job.powers) # TEMPORARY: DISABLED JOBS
		self.title=self.job.title
		self.feelingNo=0
		
	def describe(self):
#		print "aoranisReturning>"+aOrAn(self.title)
		tale.state([self.name,"was",aOrAn([self.title])])
	def actOn(self,other):
		action = oneOf(list(self.powers))
		tale.state([self.name,action[0],other.name])
		other.feelingNo += action[1]
	def feel(self):
		### feelings for others are negative. feelings for self are positive
#		tale.state([str(self.feelingNo)])
		if self.feelingNo>12:
			feelings="blinded by selfishness"
		elif self.feelingNo>8:
			feelings="very selfish"
		elif self.feelingNo>6:
			feelings="selfish"
		elif self.feelingNo>2:
			feelings="self-centered"
		elif self.feelingNo>0:
			feelings="self-aware"
		elif self.feelingNo==0:
			feelings="good"
		elif self.feelingNo>-2:
			feelings="small"
		elif self.feelingNo>-2:
			feelings="very small"
		elif self.feelingNo>-6:
			feelings="tiny"
		elif self.feelingNo>-8:
			feelings="streteched"
		elif self.feelingNo>-12:
			feelings="crushed"
		else:
			feelings="dead"
		tale.state([self.name,"felt",feelings])

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

names=["Jim","Karl","Pharaoah","Queenie","Marty","Doctor Brown","Empressette","Proffessor Plum","Wifty","Beefy","Bobert","Maxwell","Denvod","Clix","Amias the Third","Bobiatas"]
def getName(): # fairly ### doesn't work if you use everybody!
#	forenames=["Jon","Jim","Karl"] ### add this functionality later
	global names
	randomNameNo = oneIn(len(names))
	randomName = names[randomNameNo]
	del names[randomNameNo] #removing element from list so we don't get repeats in the story
	return randomName

################ randomisers ###############################

seeds = [] # string based randomiser setup
lastSeed = -1

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

### Other Global Variables:

humanNaturalPowers=[
["saved",+5],
["inspired",+4],
#["listened to",+3],
["read a story to",+3],
["greeted",+2],
#["played a game with",+2],
["complemented",+1],
["frowned at",-1],
["insulted",-2],
["shouted at",-3],
["stood on",-4],
["captured",-5]
##["murdered",-100], ## DISABLED... Causing too many killings!
]

# DEPRICATED
properNouns=["Jim","Karl","Pharaoah","Queenie","Marty","Doctor Brown","Empressette","Proffessor Plum","Wifty","Beefy","Bobert","Maxwell","Denvod",
               "Clix","Amias the Third","Bobiatas"]

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

#proffessions=[
#assasin

### run main

tale = story()

main()

############ old functions
'''
def threeActStory():

	global properNouns
	global commonNouns
	global nouns
	global badVerbs
	global goodVerbs
	global verbs
	global badAdverbs
	global goodAdverbs
	global prep1
	global prep2
	global goodAdjectives
	global badAdjectives

	protagonist=oneOf(properNouns)
	sidekick=oneOf(properNouns)
	antagonist=oneOf(properNouns)
	firstAffected=oneOf(nouns)

# Three Act Structure
	story = ["\n", #firstact
	state([protagonist, "was", aOrAn([oneOf(goodAdjectives,2) + oneOf(commonNouns)]) ]),
	state([protagonist, oneOf(goodVerbs), sidekick, "(", aOrAn([oneOf(goodAdjectives,2), oneOf(commonNouns)]), ")"]),
	state([antagonist, " was", aOrAn([oneOf(badAdjectives,2) + oneOf(commonNouns)]) ]),
	state([antagonist, oneOf(badAdverbs,3), oneOf(badVerbs), sidekick]),
	state([protagonist, oneOf(goodAdverbs,3), oneOf(goodVerbs), sidekick]),
	"\n", #secondact
	state([antagonist, oneOf(badAdverbs,3), oneOf(badVerbs), protagonist]),
	state([sidekick, oneOf(goodAdverbs,3), oneOf(goodVerbs), protagonist]),
	"\n", #thirdact
	state([protagonist, oneOf(badAdverbs,3), oneOf(badVerbs), antagonist]),
	state([protagonist, oneOf(goodAdverbs,3), oneOf(goodVerbs), sidekick]),
	"\n"] #theEnd

	return "".join(story)
'''
#hello
