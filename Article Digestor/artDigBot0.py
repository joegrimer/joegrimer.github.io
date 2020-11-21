#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  Article Digestor - At the moment, a simple word-connections "AI"
#  Copyright 2016 Joseph Grimer <joe@CaveTroll>

############################## Libraries ######################################

############################## Global Vars ####################################

############################## Main Functions #################################

continueRunning=True

def main():

	print("Welcome to Ad - son of Ai. Talk to me, so that I may learn your ways.")
	
	while True:
		paragraphs = raw_input("> ") # this is a random sit on the keyboard string
		if continueRunning==False:
			break
		sentences = paragraphs.split(".")
		print(sentences) # (example 2 from BBC News)")

	words = sentence.split(" ")
	wordConnections = {}
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

	print wordConnections
	print ("\n--------------------------------------\n")
	output = ["John"] # eventually random caps word from dict
	nextSearch = wordConnections["John"][-1]
	for i in range(0,98):
		if nextSearch in wordConnections:
			output.append(nextSearch)
#			print(wordConnections(nextSearch))
#			for each in 
			nextSearch = rollFor(wordConnections[nextSearch])
	
	print(" ".join(output)) # flush

	return 0

############################## Active Functions ###############################

randStr = 997
def rollFor(array): # randomness thing
	global randStr
	randStr+=997
#	print("raning at" + str(randStr%len(array)))
	return array[randStr%len(array)]

############################## Prep Functions #################################



if __name__ == '__main__':
	main()
















