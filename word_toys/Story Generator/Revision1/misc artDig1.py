#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  Article Digestor - At the moment, a simple word-connections "AI"
#  Copyright 2016 Joseph Grimer <joe@CaveTroll>

# version 1. Current intention: To use grammar, logic and rhetoric to build a story in English.

############################## Libraries ######################################

############################## Global Vars ####################################

############################## Main Functions #################################

def main():

	print("Welcome to Ad - son of Ai. My purpose is to generate an interesting story for you :D")
	print("No external input has been used.") # (example 2 from BBC News)")
	
#	generate world
	environments=["rainforest","desert","cave","forest","mountain"]
	initialPlace=pickFrom(environments)
	print("John lived in "+initialPlace)
	print("Monster came to the "+initialPlace)
	print("John killed monster")	

############################## Essences ########################################

#class environment():
#	

############################## Non-Main Functions ##############################

randStr = 9975
def pickFrom(array): # randomness thing
	global randStr
	randStr+=971
#	print("raning at" + str(randStr%len(array)))
	return array[randStr%len(array)]

############################## Prep Functions #################################



if __name__ == '__main__':
	main()
















