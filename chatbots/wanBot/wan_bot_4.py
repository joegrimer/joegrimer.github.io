# Jeeves - Joseph Grimer - 12 Jul 2016

#if where is or what is in then associative array
#if it is in then add element
#use formal logic principles - all A is B, all B is C: All A is C
#Neural-network type system (numbers, weights etc.)?
#Evolutionary Algorithms?
#Break down phrases via standard grammar...
#to create nodes based on grammatical structure.
#-------------------------------
# common and proper noun, more logical terms.
# proper = lowest level. common = anything higher (universal)

print("Hello World... Wan here... preparing for duty")

import re
allData=[] # main object
response='----------------------\n  My Response Begins:\n'

class thing:
  form = "unknown"

def main():
#  respondTo("Welcome to Earth. Who are you?")
#  respondTo("Alpha is Beta. Beta is Gamma. Gamma is Delta. Delta is Epsilon. delta is what.alpha is what.what is delta")
#  respondTo("Where is in England. Berkshire is in where")
  laptop = thing()
  print laptop.form

def respondTo(input):
  global response
  inputAry = input.split(".")

  for sentence in inputAry:
    if (sentence == ""):
      continue

    print(sentence.strip())
    phrases=sentence.split(" is in ")

#    splitup=re.search('(What)',sentence)
#    if splitup:
#      print "SPLITUPPOSITIVE>",splitup

    if phrases[0].lower().strip() == "what":
      getSub(phrases[1].strip().lower())
    elif phrases[1].lower().strip() == "what":
      getObj(phrases[0].strip().lower())   
    else:
      allData.append([phrases[0].strip().lower(),phrases[1].strip().lower()])
    
  print(response)

def getObj(subject):
  global response
  for sample in allData:
    if sample[0]==subject.lower():
      response+="Answer(s):"+subject+" is "+sample[1]+"\n"
      return

def getSub(object):
  global response
  for sample in allData:
    if sample[1]==object.lower():
      response+="Answer(o):"+sample[0]+" is "+object+"\n"
      return

def respond(what):
  global response
  response+=what+"\n"

#Run Main:
main()
