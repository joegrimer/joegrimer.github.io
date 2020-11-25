
###############################################################################
##################### Chat Bot - Joseph Grimer 23jul2016 ######################
###############################################################################

### Version 1 - Input output + recognising forms of to be, and what is
'''
Notes:

Todo:
- is Joseph human
- proper nouns dictionary
- circles... (with things in them)
'''

################################# Imports #####################################

import time # I wish they always had time and random
#time.sleep(0.4)
import re # another very important one!
import ast # a dicationry importer??

############################# Global Variables ################################

factAry={} # used by to be, can, save() and load()
factVenn=[] # used by to be, can, save() and load()

adverbs=("perfectly","brilliantly","simply","badly","mechanically")
toBeConj=("was","were","am","are","is",)
canConj=("can","cannot",) # cannot negative exception because it's one word
prepositions=["yet","but","so"]

############################## Classes ########################################

class person: # template:Assassin
	def __init__(self): # (self,name)
		self.name="Human"
		self.attributes=[]
	def describe(self):
		story.state([self.name,self.attributes])

############################ Main Functions ###################################

def main():

	print("Welcome to Chatbot... Your Personal Digital Assistant")
	
#	promptForSeed()
	load()
#	print(factAry)

	print("Thank You. I am ready now...")
	
	while True:
		hInput = raw_input("> ") # this is a random sit on the keyboard string
		if processInput(hInput)==False:
			break
	
	### temporary
#	hInput = raw_input("> ") # this is a random sit on the keyboard string
#	processInput(hInput)

	makeVenn()
		
	save()

def processInput(hInput):

	global toBeConj

	if hInput.lower() in ["quit","q","exit"]:
		print("Goodbye")
		return False
	elif hInput.lower() in ["hi","hello"]:
		print("Hello")
	
	words = hInput.split(" ")
#	print(words)

	sentenceStage=0
	subj=[]
	verb=[]
	obj=[]
	for word in words:
		#start capturing subject
		if sentenceStage==0:
			if word in toBeConj: # what about adverbs?
				sentenceStage=2
			else:
				subj.append(word)
		if sentenceStage==1:
			verb.append(word)
		if sentenceStage==2:
			obj.append(word)
#		if word in toBeConj:
#			#start capturing object
#			somethingIs(words)
#		elif word in canConj:
#			somethingCan(words)
#	else:
#		print "Oh Really?"
	print "S" + str(subj) + "V" + str(verb) + "O" + str(obj)

def somethingIs(words):
	global factAry
	sentenceStr = " ".join(words)
	[subj,obj]=re.split(' am | are | is ',sentenceStr)
#	[subj,obj]=sentenceStr.split("am|is")
#	print(subj)
#	print(obj)
	subj=subj.strip()
	obj=obj.strip()
	objWords=obj.split(" ")
	if objWords[0] == "not":
#		factAry[subj]=[] #reset it
		del factAry[subj]
	elif obj == "what":
		for attribute in factAry[subj]:
			print subj + " is " + attribute + ". "
	elif(subj in factAry):
		factAry[subj].append(obj)
	else:
		factAry[subj]=[obj]
	print factAry

def somethingCan(words):
	global factAry
	sentenceStr = " ".join(words)
	[subj,obj]=re.split(' can',sentenceStr)
	subj=subj.strip()
	obj=obj.strip()
	objWords=obj.split(" ")
	if objWords[0] == "not":
#		factAry[subj]=[] #reset it
		del factAry[subj]
	elif obj == "what":
		for attribute in factAry[subj]:
			print subj + " " + attribute + ". "
	elif(subj in factAry):
		factAry[subj].append("can " + obj)
	else:
		factAry[subj]=["can " + obj]
	print factAry

def makeVenn():
	for subj in factAry:
		print(subj + str(factAry[subj]))
		termStr=subj + ": "
		for obj in factAry[subj]:
			if obj in factAry:
				print(factAry[obj])

############################ other functions ##################################

# example of variable to load = 
#{'i': ['fat', 'ugly'], 'you': ['fat'], 'we': ['all fat'], 'we all': ['fat']}
def load():
	file1 = open("chatBotData.txt", "r")
	fileFacts = file1.read()
#	fileFacts = fileFacts[1:-1]
#	itemByItem = fileFacts.split(", ")
#	for item in itemByItem:
#		print(item)
#	print(fileFacts)
	global factAry
	factAry=ast.literal_eval(fileFacts)
	file1.close()

def save():
	print("Saving...")
	file1 = open("chatBotData.txt", "w+") # w+ means create/write and read.
#	saveStr=""
#	for each in factAry:
#		saveStr += 
	file1.write(str(factAry))
#	file1.write(str(factVenn))
	file1.close()

################# grammar and spelling related functions ######################

def aOrAn(words): # still need to fix spaces problem
#	print(words)
	for word in words:
		if word=="":
			continue
		elif word[0].lower() in ["a","e","i","o","u"]:
			return "an " + " ".join(words)
		else:
			return "a " + " ".join(words)

############################ randomisers ######################################

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

############################# Run Main ########################################

main()

########################### Old Functions #####################################









