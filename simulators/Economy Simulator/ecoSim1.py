#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  ecoSim.py
#  
#  Copyright 2016 Joseph Grimer <joe@CaveTroll>
#  

from random import choice # originally I wrote my own random funcs, but they had prime number problems!
#print(choice(["0","9"]))

############################### main Functions ################################

balance = 1000.00 #balance
bitcoinsOwned = 0
owebitcoinsOwned = 0
currentPrice = 1000 #pence
priceGraph=[currentPrice]
thirdBiases = []
dateNo = 0 #instantly incremented anyway
hourNo = 0
personalStatement = "£1000\t.\t.\t.\t.\tStarting Investment"

def main():

	print("-------------------------------------------------------------------"
	+"\n               Welcome to Currency Trade Simulator"
	+"\n-------------------------------------------------------------------"
	+"\n|                           __  _        |               (Predicted)"
	+"\n|   __           970.9 --- /  \\/ \\       |                (Outcome)"
	+"\n|  /  \\                   /       \\     1pm                      "
	+"\n| /    \\                 /         \\  (Lunch)            ?      "
	+"\n|/      \\          _/\\__/           \\    |              ? ?       ?"
	+"\n|        \\_       /                  \\   |             ?   ?     ? "
	+"\n|8 am      \\     /                    \\  |   _/\      ?     ?   ? "
	+"\n|Open       \\/\\_/                      \\ |  /   \\/\\  ?       ? ?"
	+"\n|                ---964.4               \\/\\/       ??         ?"
	+"\n-------------------------------------------------------------------"
	+"\nYour Challenge: Double your money in 28 days by speculating\non the price of Bitcoins on the Currency Market.")

	global thirdBiases
	thirdBiases = genBiases(8)
	lon = genBiases(8)
	tok = genBiases(8)
	nyk = genBiases(8)
	weekDays = genBiases(6)
	
	global balance
	global dateNo
	global hourNo

	print("You start with £"+str(balance)+"0 British Pounds")
	print("Initial Price per Bitcoins: £10.00"
	+"\n-------------------------------------------------------------------")

	for i in range(4): #four weeks
		for j in weekDays: #6 days in an economic week
			dateNo+=1
			print(makeDate())
			print("\n----------\t-----------\tLONDON:\t---------\t-----------")
			runThird(lon,j)
			print("\n----------\t-----------\tTOKYO:\t---------\t------------")
			runThird(tok,j)
			print("\n----------\t-----------\tNEW YORK:\t--------\t----------")
			runThird(nyk,j)
			dailyReport()
			printPersonalStatement()
#			if balance<0:
#				return
			hourNo=0
		dateNo+=1
		sundayReport() # SUNDAY WEEKLY REPORT
	print("You finished with "+str(balance)+" British Pounds")
	print("That is "+str(balance/10)+"% of your original investment")
	if(balance>=2000):
		print("So you Won! Congratulations! Now you can quit for life!")
	else:
		print("So you lost mate... now go get a proper job!")

	return 0

########################### In Game Functions #################################

def makeDate():
	global dateNo
	date = dateNo
	dayNo = dateNo%7
	noForDay = {
		0: "Sunday",
		1: "Monday",
		2: "Tuesday",
		3: "Wednesday",
		4: "Thursday",
		5: "Friday",
		6: "Saturday",
    }
	return str(noForDay.get(dayNo)) + " the "+ str(date) + "th of April 2013"

def runThird(region,weekDayBias):
	global currentPrice
	global thirdBiases
	global priceGraph
	directions=[-2,-1,0,+1,+2] #pence
	for hourBias, regionBias in zip(thirdBiases, region):
#		if balance<0:
#			return
#	for hourBias in dayBias:
		randomMarketChange = choice(directions)
		currentPrice = currentPrice+randomMarketChange+hourBias+regionBias+weekDayBias #also a type of hour bias
		broker()
		priceGraph+=[currentPrice] #1 pound

def dailyReport():
	print("---------------------- The Daily Speculator ----------------------"
	+"\nToday, bitcoinsOwned kicked off in London at "+str(priceGraph[-25])
	+"\n going into Tokyo at "+str(priceGraph[-17])
	+"\n and greeting the Yankies at "+str(priceGraph[-9])
	+"\nCurrently, it's flying at "+str(priceGraph[-1])
	+"\nGood Luck for tomorrow. You're gonna need it!"
	+"\n-----------------------------------------------------------------")
	startingPrice = priceGraph[-24]
#	for i in priceGraph[-24:-1]:
#		graph=""
#		for j in range(i-900):
#			graph+=" "
#		graph+="|"
#		print(graph)
	
def sundayReport():
	print("----------------------- The Weekly Report ------------------------"
	+"\nOn Monday, bitcoinsOwned started out at a healthy "+str(priceGraph[-145])
	+"\n Tuesday: Having second thoughts for "+str(priceGraph[-121])
	+"\n Wednesday: spinning around "+str(priceGraph[-97])
	+"\n Thursday: dancing on "+str(priceGraph[-73])
	+"\n Friday: hoping at "+str(priceGraph[-49])
	+"\n Saturday: leading with "+str(priceGraph[-25])
	+"\nCurrently, it's swimming at "+str(priceGraph[-1])
	+"\nGood Luck for next week. Now go get some tea!"
	+"\n-----------------------------------------------------------------")
	startingPrice = priceGraph[-24]

def debitAccount(currentPrice,coins):
	global balance
	global bitcoinsOwned
	global personalStatement
	balance -= coins*(float(currentPrice)/100)
	personalStatement+=("\n£"+str(balance)+"\t" + str(bitcoinsOwned)+" Bitcoins \t"+str(hourNo)+":00 "+makeDate())

def printPersonalStatement():
	print("------------ Nationarrow Bank: Your Personal Statement-----------")
	print(personalStatement)
	print("\n-------------------------------------------------------------")

def broker():
	global bitcoinsOwned
	global owebitcoinsOwned
	global hourNo
	global balance
	print("You have £"+str(balance)+" and "+str(bitcoinsOwned)+" Bitcoins. Current Price is £"+str(float(currentPrice)/100))
	choice = raw_input(str(hourNo)+":00 Hours - How many Bitcoins would you like to buy/sell?")
	if choice!="":
		coins = int(choice)
		bitcoinsOwned += coins
		debitAccount(currentPrice,coins)
		# charge interest
		if balance<0:
			print("You have made a transaction with a negative balance. You have been charged £"+str(-balance*0.01)+" in interest")
			balance=balance*1.01 # 1% interest every transaction
		if bitcoinsOwned<0:
#			debitAccount(currentPrice*0.01,bitcoinsOwned) #1% interest
			balance+=float(currentPrice)/100*bitcoinsOwned*0.01 # 1% interest
			print("You are borrowing bitcoins. You have been charged £"+str(float(currentPrice)/100*-bitcoinsOwned*0.01)+" in interest")
	hourNo+=1
	printStats()

def printStats():
	global priceGraph
	# find max/min
	max=1000
	min=1000
	for i in priceGraph:
		if i > max:
			max = i
		elif i < min:
			min = i
	print("------------------------------------------------------------------")
	for i in range(min,max+1):
		line = ""
		for j in priceGraph:
			if(i==j):
				line+="-"
			else:
				line+=" "
		print(line)
#		print("")
	print("------------------------------------------------------------------")
	print(priceGraph)

############################ Preperation Functions ###########################

def genBiases(quantity): #generates an 8 hour day structure overlay
#	return [-1, -1, -1, -1, 1, 1, 1, 1]
	biases = []
	directions=[-1,0,+1] #pence
	mean = 0
	for i in range(quantity,0,-1):
		randDir = choice(directions)
		if(abs(mean+randDir)>=i):
			if(mean==0):
				randDir=0
			elif(mean<0):
				randDir=1
			else:
				randDir=-1

		mean+=randDir
		biases.append(randDir)
	return biases

if __name__ == '__main__':
	main()
















