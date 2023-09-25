#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  PROGRAM NAME - PURPOSE
#  Copyright 2016 Joseph Grimer <joe@CaveTroll>

######################## Libraries and Global Vars ############################

import time # used for Time Delays
#time.sleep(5) # delays for 5 seconds

######################## Main Functions #######################################

def main():

	print("Hello World!")

#	firstPrime = 1
	secondPrime = 41
	for firstPrime in range(0,secondPrime):
#		firstPrime = 1
#		secondPrime = 37
		tempFirstPrime = firstPrime

		theAry = []
		for h in range(0,secondPrime):
			theAry.append(".")
		for i in range(0,secondPrime):
			if theAry[tempFirstPrime%secondPrime] == ".":
				theAry[tempFirstPrime%secondPrime] = "O"
			else:
				print("disproof")
			tempFirstPrime += firstPrime
			print("".join(theAry))
		print("".join(theAry))
		time.sleep(.25) # delays for 5 seconds


	return 0

######################## Active Functions #####################################



######################## Prep Functions #######################################



######################## Other Functions ######################################



######################## Main Functions #######################################

if __name__ == '__main__':
	main()

