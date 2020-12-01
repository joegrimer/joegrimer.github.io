#!/usr/bin/env python3
#
#  ecoSim.py
#  
#  Copyright 2016 Joseph Grimer <joe@CaveTroll>
#  This is an economy simulator I wrote on 18/11/2016 (mostly). I'm quite happy with it, I must admit!

# Joseph Grimer - 21/1/2016

'''

Ideas for further improvement:
Before the game starts, detirmine which factors will affect the economy. The news will talk about what's happening. Most of it will be irrelevant. However, some of the factors will have direct affect (plus or minus a chaos factor) on the price of whatever is being bought.

'''

from random import choice # originally I wrote my own random funcs, but they had prime number problems!

balance = 1000.00 #balance
bitcoins_owned = 0
owe_bitcoins_owed = 0
currentPrice = 1000 #pence
price_graph=[currentPrice]
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
   +"\nYour Challenge: Double your money in 28 days by speculating\non the price of Bitcoins on the Currency Market."
   +"\nGood luck, and never forget that the market only ever seems random")

   global thirdBiases
   thirdBiases = gen_biases(8)
   lon = gen_biases(8)
   tok = gen_biases(8)
   nyk = gen_biases(8)
   weekDays = gen_biases(6)
   
   global balance
   global dateNo
   global hourNo

   print("You start with £"+str(balance)+"0 British Pounds")
   print("Initial Price per Bitcoins: £10.00"
   +"\n-------------------------------------------------------------------")

   for i in range(4): #four weeks
      for j in weekDays: #6 days in an economic week
         dateNo+=1
         print(make_data())
         print("\n----------\t-----------\tLONDON:\t---------\t-----------")
         runThird(lon,j)
         print("\n----------\t-----------\tTOKYO:\t---------\t------------")
         runThird(tok,j)
         print("\n----------\t-----------\tNEW YORK:\t--------\t----------")
         runThird(nyk,j)
         dailyReport()
         print_personal_statement()
#        if balance<0:
#           return
         hourNo=0
      dateNo+=1
      sunday_report() # SUNDAY WEEKLY REPORT
   print("You finished with "+str(balance)+" British Pounds")
   print("That is "+str(balance/10)+"% of your original investment")
   if(balance>=2000):
      print("So you Won! Congratulations! Now you can quit for life!")
   else:
      print("So you lost mate... now go get a proper job!")

   return 0

########################### In Game Functions #################################

def make_data():
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
   global price_graph
   directions=[-2,-1,0,+1,+2] #pence
   for hourBias, regionBias in zip(thirdBiases, region):
#     if balance<0:
#        return
#  for hourBias in dayBias:
      randomMarketChange = choice(directions)
      currentPrice = currentPrice+randomMarketChange+hourBias+regionBias+weekDayBias #also a type of hour bias
      broker()
      price_graph+=[currentPrice] #1 pound

def dailyReport():
   print("---------------------- The Daily Speculator ----------------------"
   +"\nToday, bitcoins_owned kicked off in London at "+str(price_graph[-25])
   +"\n going into Tokyo at "+str(price_graph[-17])
   +"\n and greeting the Yankies at "+str(price_graph[-9])
   +"\nCurrently, it's flying at "+str(price_graph[-1])
   +"\nGood Luck for tomorrow. You're gonna need it!"
   +"\n-----------------------------------------------------------------")
   startingPrice = price_graph[-24]
#  for i in price_graph[-24:-1]:
#     graph=""
#     for j in range(i-900):
#        graph+=" "
#     graph+="|"
#     print(graph)
   
def sunday_report():
   print("----------------------- The Weekly Report ------------------------"
   +"\nOn Monday, bitcoins_owned started out at a healthy "+str(price_graph[-145])
   +"\n Tuesday: Having second thoughts for "+str(price_graph[-121])
   +"\n Wednesday: spinning around "+str(price_graph[-97])
   +"\n Thursday: dancing on "+str(price_graph[-73])
   +"\n Friday: hoping at "+str(price_graph[-49])
   +"\n Saturday: leading with "+str(price_graph[-25])
   +"\nCurrently, it's swimming at "+str(price_graph[-1])
   +"\nGood Luck for next week. Now go get some tea!"
   +"\n-----------------------------------------------------------------")
   startingPrice = price_graph[-24]

def debit_account(currentPrice,coins):
   global balance
   global bitcoins_owned
   global personalStatement
   balance -= coins*(float(currentPrice)/100)
   personalStatement+=("\n£"+str(balance)+"\t" + str(bitcoins_owned)+" Bitcoins \t"+str(hourNo)+":00 "+make_data())

def print_personal_statement():
   print("------------ Nationarrow Bank: Your Personal Statement-----------")
   print(personalStatement)
   print("\n-------------------------------------------------------------")

def broker():
   global bitcoins_owned
   global owe_bitcoins_owed
   global hourNo
   global balance
   print("You have £"+str(balance)+" and "+str(bitcoins_owned)+" Bitcoins. Current Price is £"+str(float(currentPrice)/100))
   choice = raw_input(str(hourNo)+":00 Hours - How many Bitcoins would you like to buy/sell?")
   if choice!="":
      coins = int(choice)
      bitcoins_owned += coins
      debit_account(currentPrice,coins)
      # charge interest
      if balance<0:
         print("You have made a transaction with a negative balance. You have been charged £"+str(-balance*0.01)+" in interest")
         balance=balance*1.01 # 1% interest every transaction
      if bitcoins_owned<0:
#        debit_account(currentPrice*0.01,bitcoins_owned) #1% interest
         balance+=float(currentPrice)/100*bitcoins_owned*0.01 # 1% interest
         print("You are borrowing bitcoins. You have been charged £"+str(float(currentPrice)/100*-bitcoins_owned*0.01)+" in interest")
   hourNo+=1
   print_stats()

def print_stats():
   global price_graph
   # find max/min
   max=1000
   min=1000
   for i in price_graph:
      if i > max:
         max = i
      elif i < min:
         min = i
   print("------------------------------------------------------------------")
   for i in range(min,max+1):
      line = ""
      for j in price_graph:
         if(i==j):
            line+="-"
         else:
            line+=" "
      print(line)
#     print("")
   print("------------------------------------------------------------------")
   print(price_graph)

############################ Preperation Functions ###########################

def gen_biases(quantity): #generates an 8 hour day structure overlay
#  return [-1, -1, -1, -1, 1, 1, 1, 1]
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
















