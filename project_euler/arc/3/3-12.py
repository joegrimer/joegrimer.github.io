#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  PROGRAM NAME - PURPOSE
#  Copyright 2016 Joseph Grimer <joe@CaveTroll>
# 3.5 going back to divided by, as opposed to chunking
# 0.009 seconds - most efficient yet... time for the biggie
# real program better but still takes forever but I think it works...
# biggie score: 0.152 and this one actually works!!!
# version 10 - trying to remove backupFactor ary to make it more efficient
# score: 0.173 meh!

# ways of going further:
# chunking, but eliminating factors (thereby saving time)
# using the square root as the max (how did I not think of that??)

######################## Libraries and Global Vars ############################



######################## Main Functions #######################################

def main():

	print("Euler Project #3.5:")
	
#	bigNum = 13195
	bigNum = 600851475143
	print(str(bigNum)+"'s largest prime factor is "+str(largestPrimeFactor(bigNum)))
#	print(str(bigNum)+" is prime? "+str(isPrime(bigNum))) # no! fail!
	
	return 0

######################## Active Functions #####################################


# runs forwards and mods instead of chunking, as that is faster
def largestPrimeFactor(subject):

	pFactor=2 # first factor to check
	while 1:
		quotient = subject/pFactor
		product = quotient*pFactor
#		print"fac " + str(pFactor) +" q " + str(quotient) + "sub "+str(subject)+ " max is " + str(subject/(pFactor-1))
		if product==subject: #then it's a factor
#			print "#######################################ISfactor"+str(quotient)
			if isPrime(quotient): # then it's our highest prime factor
				return quotient
			elif isPrime(pFactor): # possibly helpful, we don't know yet
				backupFactor=pFactor
#				print "NOT PRIME.. Plan B is"+str(backupFactors[-1])

		pFactor+=1
		if pFactor>=subject/(pFactor-1): #(i.e. eliminating innefficiency #I need this to be stored, co I'm not calculating twice
#			print "#innefficiency eliminated, max is " + str(subject/(pFactor-1))
#			print "starting plan B (backup factors are)" + str(backupFactors)
			if (backupFactor):
				return backupFactor
			#else
#			print "but they are sadly not prime..."
			break

	return "none" #or subject

def isPrime(subject):
#	print "testing if %s is prime"% subject
	pFactor=2
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

