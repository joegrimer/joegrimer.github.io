
############################################################################
################## Story Generator - Joseph Grimer 2016 ####################
############################################################################

'''

just having fun here... future functionlity
- currently everything in past tense... and conjugations haven't kicked in.
- pass in a body of text, and create a story from it... that's what I really want!

Two defining principles of generated story interaction:
golden rule: love thy neighbour as thyself?
silver rule??
'''

#from vocabulary import * #importa all vocab vars

######### Classes ###########

class story:
	def __init__(self): # (self,name)
		self.title="A Tale of Woe"
		self.lines = []
	def state(self,ary):
	#	print("-".join(ary))
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
		self.name=oneOf(properNouns)
		self.powers=humanNaturalPowers # natural verbs/abilities
		self.job=profession()
		self.powers.extend(self.job.powers)
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
#		tale.state([str(self.feelingNo)])
		if self.feelingNo>12:
			feelings="heavenly"
		elif self.feelingNo>6:
			feelings="amazing"
		elif self.feelingNo>2:
			feelings="brilliant"
		elif self.feelingNo>0:
			feelings="good"
		elif self.feelingNo==0:
			feelings="normal"
		elif self.feelingNo>-2:
			feelings="uneasy"
		elif self.feelingNo>-2:
			feelings="terrible"
		elif self.feelingNo>-6:
			feelings="horrible"
		elif self.feelingNo>-12:
			feelings="really horrible"
		else:
			feelings="dead"
		tale.state([self.name,"felt",feelings])
### main functions

def main():

#	alpha = person()
#	alpha.describe()

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

#	print(datetime.time.microsecond())
	threeActStory2()
	tale.recount()

def threeActStory2():

#	initiation
	protagonist=person()
	antagonist=person()
	protagonist.describe()
	antagonist.describe()
	
#	story begins:
	antagonist.actOn(protagonist)
	protagonist.actOn(antagonist)

	for i in range(1,6):
		if developStory([antagonist,protagonist]) == False:
			break
		tale.blank()
#		protagonist.feel()
#		tale.blank()
#		protagonist.actOn(antagonist)
#		antagonist.feel()
#	protagonist

def developStory(people): #ary
	somethingHasChanged=False
	for person in people:
		if person.feelingNo==0:
			tale.state([person.name,"is content, I no longer need to talk about him"])
		elif person.feelingNo<=-12:
			tale.state([person.name,"is dead, I no longer need to talk about him"])
		else:
			tale.state([str(person.feelingNo),"is acting"])
			person.actOn(person)
			hasSomethingChanged=True
	return somethingHasChanged
			

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

################ randomisers ###############################

seeds = [] # string based randomiser setup
lastSeed = -1

def aSeed():
	global seeds
	global lastSeed
	lastSeed += 1
	if lastSeed >= len(seeds):
#		print("clocking")
		lastSeed = 0
#	print(seeds[lastSeed])
	seeds[lastSeed]+=59
	return seeds[lastSeed]

def oneOf(ary,prob=1): # uses aSeed, and returns a no
	if aSeed()%prob == 0:
		return ary[aSeed()%(len(ary)-1)]
	else:
		return ""

def oneIn(max):
	return ((aSeed()+aSeed()+aSeed()+aSeed()+aSeed())%max) # 400-800?

#def coinFlip(): # depricate soon for oneIn
#	return "1"
#	return (aSeed()%2) #return 1 or 0?

### vars:

humanNaturalPowers=[["greeted",+2],["inspired",+4],["lifted",+1],["stood on",-3],["punched",-2],["kicked",-2],["saved",+8],["played a game with",+2],["listened to",+3],["read a story to",+3],["assisted",+4],["shouted at",-3],["complemented",+1],["insulted",-2],
["murdered",-100],
["loved",+6]]

properNouns=["Jim","Karl","Pharaoah","Queenie","Marty","Doctor Brown","Empressette","Proffessor Plum","Wifty","Beefy","Bobert","Maxwell","Denvod",
               "Clix","Amias the Third","Bobiatas"]

#		self.title=oneOf(["builder","assasin","juggler","programmer","musician","tailor","seamstress","cook","salesman"])
professions=[
[ "assasin",[["shot at",-6],["shot",-100],["threatened",-4],["aimed at",0],["fell in love with",+12]] ],
[ "cook",[["baked a cake for",+3],["made a tea for",+1],["made a coffee for",+2],["made dinner for",+2]] ],
[ "fairy",[["blessed",+3],["resurreced",+100],["liquified",-100],["gave fairy dust to",+6],["appeared to",+1],["cursed",-4]] ],
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
