#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  PROGRAM NAME - PURPOSE
#  Copyright 2016 Joseph Grimer <joe@CaveTroll>
# 3.5 going back to divided by, as opposed to chunking
# 0.012 seconds
# 0.009 seconds
# real program better but still takes forever

######################## Libraries and Global Vars ############################



######################## Main Functions #######################################

def main():

	print("Euler Project #3.5:")
	
#	bigNum = 101
	bigNum = 13195
#	bigNum = 600851475143
	'''
	pFactor=bigNum-1 # /2 without remainder?
	while 1:
		if bigNum%pFactor==0 and isPrime(pFactor):
			break
		pFactor-=1
		
	print "The Largest one: " + str(pFactor)
	'''
	print(str(bigNum)+"'s largest prime factor is "+str(largestPrimeFactor(bigNum)))
	
	return 0

######################## Active Functions #####################################


# runs forwards and mods instead of chunking, as that is faster
def largestPrimeFactor(largeNumber):

#	for pFactor in range(2,largeNumber-1): #everything except 1 and the numbre itself
	pFactor=2
	maxFactor=largeNumber
#	for i in [1,2,3,4,5,6,7,8,9,10]:
	while 1:
		quotient = largeNumber/pFactor
		product = quotient*pFactor
#		print"cur bigNum fac = " + str(pFactor) +" quotient " + str(quotient)
		if product==largeNumber and isPrime(quotient): # then it's a factor! This seems long winded, but I think it's right
			return quotient
		else:
			maxFactor = pFactor*(quotient-1)
		if pFactor>=maxFactor:
			break
		else: #not strictly neccessary
			pFactor+=1
	return 1 #or largeNumber

def isPrime(pPrime):
	pFactor=2
	maxFactor=pPrime
#	for i in [1,2,3,4,5,6,7,8,9,10]:
	while 1:
		quotient = pPrime/pFactor
		product = quotient*pFactor
#		print "cur pFactor = " + str(pFactor) +" product " + str(quotient) + " max is " + str(maxFactor)
		if product==pPrime: # then it's a factor! This seems long winded, but I think it's right
			return 0 #notPrime
		else:
			maxFactor = pFactor*(quotient-1)
		if pFactor>=maxFactor:
			break
		else: #not strictly neccessary
			pFactor+=1
	return 1 #prime
	
	

######################## Prep Functions #######################################



######################## Other Functions ######################################



######################## Main Functions #######################################

if __name__ == '__main__':
	main()

