# RPG - Joseph Grimer - 15 Jul 2016
# simple RPG
# todo - pub key (antiRainbowTables) the responses

#["",""],
responses = [
["hello","hello to you too!"],
["hi","How casual of you... though I salute you also!"],
["who","Me? I am Joseph Grimer. That's who I am. And if this"],
["what","This is a response device, not unlike the (addmittedly more cool) one used in iRobot. One of my favourite films as of 15 jul 2016"],
["when","When? I write this program in July 2016... and I don't know what time it is now. Well, the program tells me that it is: TODO FUNCTION, but that's just clever programming... And I am only roughly aware of it when I write this"],
["where","Where? I programmed this in that dusty old house on the south coast"],
["why","Why? for fun... for memories... for a thing. Because it's cool. For the greater glory of God! Or as close as possible..."],
["how","How? How did I come into existence? Efficient Causality, a wonderful thing (though that's avoiding the question)"],
["die","You speak of death? All I can say for that concept is: God Willing? So be it. God Bless"],
["happy","Well I'm no hedonist, but I aim for happiness too... Truth, Goodness and Beauty (and all that cool philosophical stuff)"],
["sad","Don't be sad. But be happy in the truth, whatever it may be. Never fear the truth. Understand it, embrace it (and don't forget to look for goodness and beauty), and you will find happiness."],
["life","Death is a natural part of life."],
["soul","The soul id the animator... that which moves. So in a way, scientific laws are essentially souls"],
["return","The Resturn of Zorro was a terrible film... and the Return of the Jedi was okay... but a true return: That will be quite spectacular!"],
#["",""],
["good","God is Good :)"]]

newResponses = []

key = "'|}{'\[]AHTDH(BOI&"
keyIndex = 0

print "Hullo... This is an if message encoder"

for response in responses:
  newResponses.append([""])
  keyNo = 0
  wordInd = 0
  wordLen = len(response[0])
  
  ## note: biggest ascii code 255?
#  for letter in response[1]:
  for letter in response[1]: # trigger word
#    print "wordInd"+str(wordInd)
#    print ord(response[0][wordInd])
    keyNo += ord(response[0][wordInd])
    
#    print "key is "+ str(keyNo)+"... and letter is " + str(ord(letter)) + "so sum is" + str(((keyNo+ord(letter))%255))
    wordInd+=1
    
    if wordInd >= wordLen:
      wordInd = 0
#  print "total"+str(keyNo)

print(newResponses)
    
#Run Main:
#main()
