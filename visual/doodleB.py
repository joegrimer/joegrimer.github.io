#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  Doodle B - Vertical game of life algorithm
#  Copyright 2016 Joseph Grimer <joe@CaveTroll>

######################## Libraries and Global Vars ############################

import time # used for Time Delays
#time.sleep(5) # delays for 5 seconds

######################## Main Functions #######################################

def main():

	print("Hello World!")
	
	secondPrime = 83
	theAry = []
	for h in range(0,secondPrime):
		theAry.append(" ")
	print("".join(theAry))

	for i in range(0,secondPrime*6): #secondPrime):
		time.sleep(0.1) # delays for 5 seconds
		newAry = theAry[:]
		for j in range(0,secondPrime):
#			print([theAry[j-1],theAry[j]])
			if [theAry[j-2],theAry[j-1],theAry[j]] == [" "," "," "]:
				newAry[j-2],newAry[j-1],newAry[j] = " ","-"," "
			elif [theAry[j-2],theAry[j-1],theAry[j]] == ["*"," ","*"]:
				newAry[j-2],newAry[j-1],newAry[j] = "-"," ","+"
			elif [theAry[j-2],theAry[j-1],theAry[j]] == ["*"," ","+"]:
				newAry[j-2],newAry[j-1],newAry[j] = " ","*"," "
			elif [theAry[j-2],theAry[j-1],theAry[j]] == ["-"," ","+"]:
				newAry[j-2],newAry[j-1],newAry[j] = " ","*"," "
			elif [theAry[j-2],theAry[j-1],theAry[j]] == [" ","-"," "]:
				newAry[j-2],newAry[j-1],newAry[j] = " ","+"," "
			elif [theAry[j-2],theAry[j-1],theAry[j]] == [" ","+"," "]:
				newAry[j-2],newAry[j-1],newAry[j] = " ","*"," "
		theAry=newAry
		aryStr = ''
		coinFlip=1
		for k in theAry:
			if coinFlip%3:
				aryStr=aryStr+k
			else:
				aryStr=k+aryStr
			coinFlip+=1
		print(aryStr)

	return 0

######################## Active Functions #####################################



######################## Prep Functions #######################################



######################## Other Functions ######################################



######################## Main Functions #######################################

if __name__ == '__main__':
	main()

