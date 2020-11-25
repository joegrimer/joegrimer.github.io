#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  PROGRAM NAME - PURPOSE
#  Copyright 2016 Joseph Grimer <joe@CaveTroll>
# 0.012 seconds
# real program better but still takes forever

######################## Libraries and Global Vars ############################



######################## Main Functions #######################################

def main():

	print("Euler Project #3.4:")
	
#	bigNum = 102
#	bigNum = 13195
	bigNum = 600851475143
	'''
	posFac=bigNum-1 # /2 without remainder?
	while 1:
		if bigNum%posFac==0 and isPrime(posFac):
			break
		posFac-=1
		
	print "The Largest one: " + str(posFac)
	'''
	print(str(bigNum)+"'s largest factor is "+str(largestFactor(bigNum)))
#	print(str(bigNum)+" is "+str(isPrimeOld(bigNum))+" prime")
	
	return 0

### type(o) is float
def largestFactor(posPri): # this runs backwards, as is more efficient for detirmining primes

	print("pospri"+str(posPri))
	posFac=posPri
	minFac=2
#	for i in range(0,1):
	while 1:
		curMul = 2 #current multiplier
		while 1:
			product = posFac*curMul
			print"cur posFac = " + str(posFac) +"curMul  "+str(curMul)+" (maxFac)"+str(minFac)+"product " + str(product)
			if product<posPri:
				minFac=curMul # this should make the program more efficient
			elif product==posPri:
##				print "returning"
				return posFac #false
			elif product>posPri:
##				print "breaking loop.. this is not a factor... posPri is "+str(posPri)
				break #i.e. not a factor
			curMul+=1
		if posFac<=minFac:
			break
		posFac-=1
  #else:
	return 1 #true

### type(o) is float
def isPrime(posPri): # this runs forwards, as is more efficient for detirmining primes

##	print("pospri"+str(posPri))
	posFac=2
	maxFac=posPri
##	for i in range(1,10):
	while 1:
		curMul = 2 #current multiplier
		while 1:
			product = posFac*curMul
			print"cur posFac = " + str(posFac) +"curMul  "+str(curMul)+" (maxFac)"+str(maxFac)+"product " + str(product)
			if product<posPri:
				maxFac=curMul # this should make the program more efficient
			elif product==posPri:
##				print "returning"
				return 0 #false
			elif product>posPri:
##				print "breaking loop.. this is not a factor... posPri is "+str(posPri)
				break #i.e. not a factor
			curMul+=1
		if posFac>=maxFac:
			break
		posFac+=1
  #else:
	return 1 #true

def isPrimeOld(posPri):

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

