#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  Article Digestor - At the moment, a simple word-connections "AI"
#  Copyright 2016 Joseph Grimer <joe@CaveTroll>

############################## Libraries ######################################

############################## Global Vars ####################################

knownText = ''

############################## Main Functions #################################

def main():

	print("Welcome to Stupid Bot.")

	load() #loads knownText var
	
	digestWords(knownText)
	
	while True:
	
		textInput = raw_input("What!? ")
		
		if textInput not in ["q","quit","exit","bye"]:
			digestWords(textInput)
		else:
			print("Sob... Bye")
			return 0
		# old story ending:

		basingItOn = textInput.split(" ")

#		print ("\n")
		output = [rollFor(basingItOn)] # eventually random caps word from dict
		nextSearch = wordConnections[rollFor(basingItOn)][-1]
		fullStopCount=0
		for i in range(1,300): #give up after that!
			if nextSearch in wordConnections:
				output.append(nextSearch)
	#			print(wordConnections(nextSearch))
	#			for each in 
				nextSearch = rollFor(wordConnections[nextSearch])
			else:
				nextSearch = rollFor(rollFor(basingItOn))
			if output[-1].endswith('.'):
	#			print("we got a full stop!")
				fullStopCount+=1
			if fullStopCount==3:
				break # the loop
		
		print(" ".join(output)) # flush

	return 0

############################## Active Functions ###############################

randStr = 997
def rollFor(array): # randomness thing
#	print("\n\n\nrollingFor"+str(array))
	global randStr
	randStr+=997
#	print("raning at" + str(randStr%len(array)))
	return array[randStr%len(array)]

############################## Prep Functions #################################

wordConnections = {}
def digestWords(text):
	words = text.split(" ")
	global wordConnections
	# the great word loop
	first = True
	last = ''
	for word in words:
		if first:
			last = word # and the last will be first :)
			first =  False
		else:
			if last in wordConnections:
				wordConnections[last].append(word)
			else:
				wordConnections[last] = [word]
			last = word

#	print("Data has been loaded") # (example 2 from BBC News)")


############################ other functions ##################################

def load():
	global knownText
	file1 = open("chatBotData.txt", "r")
	knownText = file1.read()
	file1.close()

#### NEED TO IMPLEMENT THIS FUNCTION EVENTUALLY I GUESS MAYBE
def save():
	print("Saving...")
	file1 = open("chatBotData.txt", "w+") # w+ means create/write and read.
	file1.write(str(factAry))
	file1.close()
	
######################### Mainer ###################

if __name__ == '__main__':
	main()
















