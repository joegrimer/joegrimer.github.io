#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  PROGRAM NAME - PURPOSE
#  Copyright 2016 Joseph Grimer <joe@CaveTroll>
# 3.5 going back to divided by, as opposed to chunking
# 0.009 seconds - most efficient yet... time for the biggie
# real program better but still takes forever but I think it works...
# biggie score: 1m:41, 0.149 seconds!!! Broken...

######################## Libraries and Global Vars ############################



######################## Main Functions #######################################

def main():

	print("Euler Project #3.5:")
	
#	bigNum = 13195
#	bigNum=3643331 # a random prime number
	bigNum = 600851475143
	print(str(bigNum)+"'s largest prime factor is "+str(largestPrimeFactor(bigNum)))
	
	return 0

######################## Active Functions #####################################


# runs forwards and mods instead of chunking, as that is faster
def largestPrimeFactor(subject):

#	for pFactor in range(2,subject-1): #everything except 1 and the numbre itself
	pFactor=2 # first factor to check
	backupFactor = 1
#	for i in [1,2,3,4,5,6,7,8,9,10]:
	while 1:
		quotient = subject/pFactor
		product = quotient*pFactor
#		print"fac " + str(pFactor) +" q " + str(quotient) + "sub "+str(subject)+ " max is " + str(subject/(pFactor-1))
		if product==subject: #then it's a factor
			if isPrime(quotient): # then it's our highest prime factor
				return quotient
			else: # possibly helpful, we don't know yet
				backupFactor=quotient

		pFactor+=1
		if pFactor>=subject/(pFactor-1): #(i.e. eliminating innefficiency
#			print "#innefficiency eliminated, max is " + str(subject/(pFactor-1)) +" current backup is " + str(backupFactor)
			if isPrime(backupFactor):
				return backupFactor
			#else
			break

	return 1 #or subject

def isPrime(subject):
#	print "testing if %s is prime"% subject
	pFactor=2
#	for i in [1,2,3,4,5,6,7,8,9,10]:
	while 1:
		quotient = subject/pFactor
		product = quotient*pFactor
#		print "cur pFactor = " + str(pFactor) +" product " + str(quotient) + " max is " + str(subject/(pFactor-1))
		if product==subject: # then it's a factor! This seems long winded, but I think it's right
#			print "not prime"
			return 0 #notPrime

		pFactor+=1
		if pFactor>=subject/(pFactor-1): #I need this to be stored, co I'm not calculating twice (i.e. eliminating innefficiency
#			print "innefficiency eliminated, max is " + str(subject/(pFactor-1))
			break
	return 1 #prime
	
	

######################## Prep Functions #######################################



######################## Other Functions ######################################



######################## Main Functions #######################################

if __name__ == '__main__':
	main()

