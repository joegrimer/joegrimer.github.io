#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  PROGRAM NAME - PURPOSE
#  Copyright 2016 Joseph Grimer <joe@CaveTroll>

######################## Libraries and Global Vars ############################

import time

######################## Main Functions #######################################

def main():

	print("Hello World!")

#	out = []

	out = genSample()


	printTest(out)

	out=runTick(out)
	out=runTick(out)
	out=runTick(out)
	out=runTick(out)
	out=runTick(out)
	out=runTick(out)

	print("2 is a little different though:")
	printTest(out)

	return 0

def genSample():
	out = []
	for i in range(0,8):
		out.append([])
		for j in range(0,8):
			if(randBin()):
				out[-1].append(0)
			else:
				out[-1].append(1)
	return out

# this function will run a conway's game of life rulset on the random-sample
def runTick(inSet):

	outSet=[]

	for i in range(0,8):
		outSet.append([])
		for j in range(0,8):
			maxWidth=len(inSet)-1
			if i==0:
				im1 = i
			else:
				im1 = i-1

			if i==maxWidth:
				ip1 = i
			else:
				ip1 = i+1

			if j==0:
				jm1 = j
			else:
				jm1 = j-1

			if j==maxWidth:
				jp1 = j
			else:
				jp1 = j+1

			neighbours=inSet[im1][jm1]+inSet[i][jm1]+inSet[ip1][jm1]+inSet[im1][j]
			+inSet[ip1][j]+inSet[im1][jp1]+inSet[i][jp1]+inSet[ip1][jp1]
			#print(neighbours)

			# Conway's Four laws
			if neighbours==3:
				outSet[-1].append(1)
			elif inSet[i][j]==1 and neighbours==2:
				outSet[-1].append(1)
			else: # lower than 2 or higher than 3
				outSet[-1].append(0)

	return outSet

######################## Active Functions #####################################

clock=11
primeOn=0
primes=[37,97,121,76459,12314467889999,2345345,234,2342,34,2453,46,786,795]
def randBin():
	global clock
	global primes
	global primeOn
	clock+=(time.clock()*primes[primeOn%len(primes)])
#	print(clock)
	primeOn+=1
	if round(clock)%2==1:
		return False
	else:
		return True

def printTest(test):
	output="--------\n"
	for each in test:
		for every in each:
			if every==0:
				output+=" "
			else:
				output+="o"
		output+="|\n"
	output+="--------"
	print(output)

######################## Prep Functions #######################################



######################## Other Functions ######################################



######################## Main Functions #######################################

if __name__ == '__main__':
	main()

