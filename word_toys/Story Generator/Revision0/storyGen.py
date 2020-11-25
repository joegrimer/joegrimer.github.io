
############################################################################
################## Story Generator - Joseph Grimer 2016 ####################
############################################################################

'''

just having fun here... future functionlity
- currently everything in past tense... and conjugations haven't kicked in.
- pass in a body of text, and create a story from it... that's what I really want!

'''

from vocabulary import * #importa all vocab vars

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

class person:
	def __init__(self): # (self,name)
		self.name=oneOf(properNouns)
		self.natPowers=["walked to","jumped at","ran at","broke","spoke to","inspired"] # natural verbs/abilities
		self.artPowers=["shot","flew at","programmed","spoke Chinese to"] # articial verbs/abilities
		self.powers=self.natPowers+self.artPowers
		self.title=oneOf(["builder","assasin","juggler","programmer","musician","tailor","seamstress","cook","salesman"])
		
	def describe(self):
		tale.state([self.name,"was"])
#		print(",".join(self.powers))
	def action(self):
		return oneOf(self.powers)

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

	global story #most important one

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

	protagonist=person()
	sidekick=person()
	antagonist=person()

# Three Act Structure
	tale.state(["hi"]) #firstact
	protagonist=person()
	protagonist.describe()

#	state([protagonist.name, "was", aOrAn([protagonist.title]) ]),
	
#	state([protagonist.name, oneOf(goodVerbs), sidekick.name, "(", aOrAn([sidekick.title]), ")"]),
#	state([antagonist.name, "was", aOrAn([antagonist.title]) ]),
#	state([antagonist.name, antagonist.action(), sidekick.name]),
#	state([protagonist.name, protagonist.action(), sidekick.name]),
#	"\n", #secondact
#	state([antagonist.name, antagonist.action(), protagonist.name]),
#	state([sidekick.name, sidekick.action(), protagonist.name]),
#	"\n", #thirdact
#	state([protagonist.name, protagonist.action(), antagonist.name]),
#	state([protagonist.name, protagonist.action(), sidekick.name]),
#	"\n"] #theEnd

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
#		print("truth")
		return ary[aSeed()%(len(ary)-1)]
	else:
#		print("falsehood")
		return ""

def oneIn(max):
	return ((aSeed()+aSeed()+aSeed()+aSeed())%max) # 400-800?

def coinFlip(): # depricate soon for oneIn
#	return "1"
	return (aSeed()%2) #return 1 or 0?

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
