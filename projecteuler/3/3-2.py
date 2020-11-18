#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  PROGRAM NAME - PURPOSE
#  Copyright 2016 Joseph Grimer <joe@CaveTroll>
# 0.011 seconds test (0.9 before I tried to make it more efficient)

######################## Libraries and Global Vars ############################



######################## Main Functions #######################################

def main():

	print("Euler Project #3:")
	
#	bigNum = 11
#	bigNum = 13195
	bigNum = 600851475143

	posFac=bigNum-1 # /2 without remainder?
	while 1:
		if bigNum%posFac==0 and isPrime(posFac):
			break
		posFac-=1
		
	print "The Largest one: " + str(posFac)
#	print(str(bigNum)+" is "+str(isPrime(bigNum))+" prime")
	
	return 0

### type(o) is float
def isPrime(posPri): # this runs forwards, as is more efficient for detirmining primes

	posFac=2
	maxFac=posPri
	while 1:
		curMul = 2 #current multiplier
		while 1:
			product = posFac*curMul
			if product<posPri:
				maxFac=curMul # this should make the program more efficient
			elif product==posPri:
				return 0 #false
			elif product>posPri:
				break #i.e. not a factor
			curMul+=1
		if posFac>=maxFac:
			break
		posFac+=1
	return 1 #true


######################## Active Functions #####################################



######################## Prep Functions #######################################



######################## Other Functions ######################################



######################## Main Functions #######################################

if __name__ == '__main__':
	main()

