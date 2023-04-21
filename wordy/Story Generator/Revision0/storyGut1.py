
############################################################################
##################  - Joseph Grimer 21 Jul 2016 ####################
############################################################################

'''
this is a story gutter... to take a fairytale, and gut it, knowing only ands, ors, ifs, and buts??
ideas:
-
'''

#from vocabulary import * #importa all vocab vars


### main function

def main():

	print("Welcome to StoryGutter.\n")

	allWords = {} # dictionary
	
	paragraphs = story.split("\n")
	for paragraph in paragraphs:
		sentences = paragraph.split(".")
		for sentence in sentences:
			phrases = sentence.split(",")
			for phrase in phrases:
				words = phrase.split(" ")
				for word in words:
					if word != "":
						if word not in allWords:
							allWords[word]=1
						else:
							allWords[word]+=1
	
	print(allWords)
	
	'''
	mixedWords=[]
	for i in range(0,30):
		mixedWords.append(oneOf(allWords))
	print(" ".join(mixedWords))
	'''

	print("below")

### other functions

##################### Tail ###########################################

### simple seeding:

def aSeed():
	global seeds
	global lastSeed
	lastSeed += 1
	if lastSeed >= len(seeds):
#		print("clocking")
		lastSeed = 0
	seeds[lastSeed]+=59
	return seeds[lastSeed]

def oneOf(ary): # uses aSeed, and returns a no... version -1
	return ary[aSeed()%(len(ary)-1)]

seeds = [] # string based randomiser setup
lastSeed = -1
seedStr = "4eg567er5zzzp4j89ed7g6nl.ef7e58oy8ilfhogbu;/gp09d/[-9hje5sgh'4689=8se"

# Prepare Randomiser
for char in seedStr:
	seeds.append(ord(char))

### globals?? ###

story="once upon a time there was a boy called John. John loved apples. One day, John found a red apple. John ate the red apple. John died."

### run main

main()

############ old functions ###########

