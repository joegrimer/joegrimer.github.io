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

import re # importing regular expression library to make splitting simpler

print("Hello World... Wan here... preparing for duty")

import re
allData=[] # main object
dict={} # word coming up dictionary
response='----------------------\n  My Response Begins:\n'

def main():
#  respondTo("Welcome to Earth. Who are you?")
#  respondTo("Alpha is Beta. Beta is Gamma. Gamma is Delta. Delta is Epsilon. delta is what.alpha is what.what is delta")
#  respondTo("Where is in England. Berkshire is in where")
  respondTo("Dom Pedro Afonso 19 July 1848 10 January 1850 was the Prince Imperial and heir apparent to the throne of the Empire of Brazil. Born at the Palace of Sao Cristovao in Rio de Janeiro, he was the second son and youngest child of Emperor Dom Pedro II and Dona Teresa Cristina of the Two Sicilies, and thus a member of the Brazilian branch of the House of Braganza. Pedro Afonso was seen as vital to the future viability of the monarchy, which had been put in jeopardy by the death of his older brother Dom Afonso almost three years earlier. Pedro Afonso's early death from fever at the age of one devastated the Emperor, and the imperial couple had no further children. Pedro Afonsos older sister Dona Isabel became heiress, but Pedro II was unconvinced that a woman could ever be accepted as monarch by the ruling elite. He excluded Isabel from matters of state, and failed to provide training for her possible role as empress. With no surviving male children, the Emperor started to believe that the imperial line was destined to end with his own death.")
  mixWords()

def respondTo(input):
  words = re.split(',\s|\.\s|\s|\.',input) # split on space (\s) and full stop (\.) 
  lastWord = ''

  for word in reversed(words):
    lowerWord = word.lower()
#    print("XX>"+lowerWord)
#    if(lastWord!=''):
    dict[lowerWord] = lastWord
      
    lastWord=lowerWord
      
  print(dict)

def mixWords():
  print("may the mixing begin!")
  wholeStr = dict.keys()[-1]
  curVar = dict.keys()[-1]
  for x in range(0, 70):
    wholeStr += (dict[curVar]+" ")
    curVar=dict[curVar]
#    del dict[curVar]
  print(wholeStr)

#  for word in dict:
#    print word
 
#Run Main:
main()
