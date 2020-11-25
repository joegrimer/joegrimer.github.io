#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  PROGRAM NAME - PURPOSE
#  Copyright 2016 Joseph Grimer <joe@CaveTroll>
# 0.01 seconds
# on real program: takes forever

######################## Libraries and Global Vars ############################



######################## Main Functions #######################################

def main():

	print("Euler Project #3:")
	
#	bigNum = 101
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
	print(str(bigNum)+" is "+str(isPrime(bigNum))+" prime")
#	print(str(bigNum)+" is "+str(isPrimeOld(bigNum))+" prime")
	
	return 0

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

