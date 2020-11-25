# RPG - Joseph Grimer - 15 Jul 2016
# ifnote 3 - 18 May 2017

responses = [
["death","What do you think death is?"],
["live","Why do we live?"],
["who","Know thyself - Artistotle"],
["what","To see 'what' is to have knowledge... but to see how is to have understanding''"],
["when","yesterday is history, tomorrow is a mystery, but today is a gift... that is why they call it the present"],
["where","Some people... aren't where we are, and some people are. But the most important question right now is: Are you?"],
["why","Purpose is deep and hard to find sometime. Meh: Boggle!"],
["how","The ticking of a clock... the firing of a gun... irrelevant. The point is: It ticks and you get shot. Now what are you going to do about it?"],
["die","Die rhymes with fly... did you know that?"],
["happy",":D"],
["sad","Sometimes it's okay to be sad... like right now. Weep for me Bob, weep for me..."],
["good","Good needs more 'o'"]
]

#solveAry = []

def main():
	print "Hullo... I am your articicial philosophical therapist."
	initiate()

	#thye loop
	while 1==1: # a bit clunk, I know
		response = raw_input(">").lower().strip()
		words = response.split(" ")

		for phrase in responses:
			if phrase[0] in words:
				print phrase[1]
				break
			elif words[0] == "quit":
				return
			else:
				print("I'm sorry.... my responses are limited (and Joe's apparently not here to fix them)... You must ask the right questions"

#Run Main:
#main()



