#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  Euler Project -4
'''


'''

def main():

  print("Euler Project #4:")
  
  print(str(findGreatPalindrome()))
  
  return 0

def findGreatPalindrome():
  solution=1
  x = 100
  while(1):
    y = 100
    while(1):
      z=x*y
      if(isPalindrome(z)):
        solution=z
#      print("xy"+str(x*y))
      if y>998:
        break
      else:
        y+=1
    if x>998:
      break
    else:
      x+=1
  return solution


def isPalindrome(pPalindrome):
	if str(pPalindrome)[::-1] == str(pPalindrome):
		return 1
	else:
		return 0
  

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
	
######################## Main Functions #######################################

if __name__ == '__main__':
	main()

