#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  PROGRAM NAME - PURPOSE
#  Copyright 2016 Joseph Grimer <joe@CaveTroll>
# 0.011seconds (test number)
# real number crashes

######################## Libraries and Global Vars ############################



######################## Main Functions #######################################

def main():

	print("Euler Project #3:")
	
	bigNum = 13195
#	bigNum = 600851475143
	factors = []
	
	for posFac in range(2,bigNum-1):
		if bigNum%posFac==0 and isPrime(posFac):
			factors.append(posFac)
			largestFactor = posFac
		
	
	print "The Factors are: " + str(factors)
	print "The Largest one: " + str(largestFactor)
	
	return 0

def isPrime(posPri):

	for posFac in range(2,posPri-1): #everything except 1 and the numbre itself
		if posPri%posFac==0: # then it's a factor!
			return 0 #false
  #else:
	return 1 #true


######################## Active Functions #####################################



######################## Prep Functions #######################################



######################## Other Functions ######################################



######################## Main Functions #######################################

if __name__ == '__main__':
	main()

