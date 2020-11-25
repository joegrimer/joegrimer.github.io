## dbot jgrimer 18May2017


def main():

	print("Hello. Welcome to D-Bot... I am convoluted")

	while True:
		input = raw_input("> ").lower()
		



'''
 #   input = input.
    if input in ["quit","q","exit"]:
      break
    else:
      #failsafe
      if input == "":
        input = "sjonwmuzla[423534634576"

      #prepare randomiser
      for char in input:
        seeds.append(ord(char))

      response = respondTo(input.split(" "))

def respondTo(input):

#  print(datetime.time.microsecond())
  print(emotionOf(input))
#  print(threeActStory())

emotionCount = 0
happyCount = 0
sadCount = 0

def emotionOf(string):
  global emotionCount
  global happyCount
  global sadCount

  global happyWords
  global sadWords
  happyWords+=["hello","happy","good","lovely","nice","beautiful","strong","intelligent","brilliant","cool","poor","pius","faith","fix","repair",
              "you","better","hi"]
  sadWords+=["fat","bad","crazy","insane","sick","death","cut","drunk","skinny","sad","judge","psychopathic","rich","proud","unethical","overweight","experimental","hate","i","bastard","die","shut","close","end","brick","kill"]
  happyVerbs=["hug","stroke","be nice to","symapthise with","kiss","give a tomato to","give a potato to","give a gift to","feed","give hope to",
  "inspire","fix","befriend","grow","crown","love","find","help","save","give up my life for","cook for","clean for","eat for","die for","make strong"
  "create","construct","solve"]
  sadVerbs=["cut","break","smash","finish","kill","crack","crush","burn","shoot","impale","skin","fry","run at","glue","bend","throw","eat","destroy",
  "gut"]

  for word in string:
#    print(">"+word+"<>"+sadWords[16]+"<")
    if word in happyWords:
#      print("word in happywords")
      emotionCount += 1
      happyCount += 1
    elif word in sadWords:
#      print("word in sadwords")
      emotionCount -= 1
      sadCount+=1

#  print(sadCount)

  words = ""

  for x in range(0,happyCount):
    words+=oneFrom(happyWords)+", I will"+oneFrom(happyVerbs)+" you.\n"
  for x in range(0,sadCount):
    words+=oneFrom(sadWords)+", I will"+oneFrom(adverbs)+oneFrom(sadVerbs)+" myself.\n"

  return words

#def threeActStory():

properNouns=["Jim","Karl","Pharaoah","Queenie","Marty","Doctor Brown","Empressette","Proffessor Plum","Wifty","Beefy","Bobert","Maxwell","Denvod",
               "Clix","Amias the Third"]
commonNouns=["egg","rock","paper","scissor","teacup","mayor","headphone","clock","lego","glue","man","box","building","friend","brick","log","tree"] #add a or the 
nouns=properNouns+commonNouns
badVerbs=["ran at","hit","shot","killed","flew at","bent","threw","stood on","broke","burned","cut","fried","slapped","crushed","discomboulated"]
goodVerbs=["changed","fixed","repaired","loved","was good to","inspired","found","was blown away by","helped","assisted","smiled at","laughed at","ate"]
verbs = goodVerbs+badVerbs
badAdverbs = ["meanly","aggresively","incompetently","spitefully","maliciously","badly","dramatically","psychopathically","dreadfully","lifelessly",
"coldly","forensically"]
goodAdverbs = ["gracefully","cleverly","hopefully","faithfully","charitably","impressively","brilliantly","intently","lovingly","perfectly",
"warmly","sunnily","moonily"]
adverbs = badAdverbs+goodAdverbs
prep1 = ["while","when","after","before","beneath","despite"]
prep2 = ["after","ontop of","over","before","beneath","despite"]
goodAdjectives = ["pretty","sympathetic","empathetic","wise","understanding","happy","strong","pius","fearing","poor","weak","humble"]
badAdjectives = ["fat","skinny","evil","bad","smelly","conked","drunk","insane","sad","judgmental","psychopathic","rich","proud","unethical",
                   "experimental"]

def aOrAn(word):
#  print(">"+word[1].lower()+"<")
  if word[1].lower() in ["a","e","i","o","u"]:
    return " an" + word
  else:
    return " a" + word

def aSeed():
  global seeds
  global lastSeed
  lastSeed += 1
  if lastSeed >= len(seeds):
#    print("clocking")
    lastSeed = 0
  seeds[lastSeed]+=59
  return seeds[lastSeed]

def oneFrom(ary): # uses aSeed, and returns a no
  return " " + ary[aSeed()%(len(ary)-1)]

def coinFlip():
#  return "1"
  return (aSeed()%2) #return 1 or 0?
'''

## run main
main()
