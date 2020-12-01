# Joseph Grimer
# Date: 18 Mar 2015
# BGG Game rater

print("Welcome to Board Game Ranker.")

gFile = open("games.txt", "r+")
#file = open("games.txt", "a")

print(gFile);

while True:

	gName = raw_input('Please name your game: ')

	print("Your game is called "+gName)

	if ((raw_input("Is " + gName + " a good game (7+)? ")[0].upper()=="Y")):
		if ((raw_input("Is " + gName + " very good (8+)? ")[0].upper()=="Y")):
			if ((raw_input("Is " + gName + " excellent (9+)? ")[0].upper()=="Y")):
				if ((raw_input("Is " + gName + " outstanding/perfect (10)? ")[0].upper()=="Y")):
					rating = 10
					print("10 - Outstanding. Always want to play and expect this will never change.")
				else:
					rating = 9
					print("9 - Excellent game. Always want to play it. ")
			else:
					rating = 8
					print("8 - Very good game. I like to play. Probably I'll suggest it and will never turn down a game.")
		else:
				rating = 7
				print("7 - Good game, usually willing to play.")
	else:
		if ((raw_input("Is " + gName + " bad (3 or less)? ")[0].upper()=="Y")):
			if ((raw_input("Is " + gName + " extremely annoying (2 or less)? ")[0].upper()=="Y")):
				if ((raw_input("Is " + gName + " absolutely awful (1)? ")[0].upper()=="Y")):
					rating = 1
					print("1 -Defies description of a game. You won't catch me dead playing this. Clearly broken.")
				else:
					rating = 2
					print("2 - Extremely annoying game, won't play this ever again.")
			else:
				rating = 3
				print("3 - Likely won't play this again although could be convinced. Bad.")
		else:
			if ((raw_input("Is " + gName + " either okay or average (5-6)? ")[0].upper()=="Y")):
				if ((raw_input("Is " + gName + " above average and okay (6)? ")[0].upper()=="Y")):
					rating = 6
					print("6 - Ok game, some fun or challenge at least, will play sporadically if in the right mood.")
				else:
					rating = 5
					print("5 - Average game, slightly boring, take it or leave it.")
			else:
				rating = 4
				print("4 - Not so good, it doesn't get me but could be talked into it on occasion.")

	if (rating!=10 and (raw_input("Is " + gName + " a little bit better than that (+.5)? ")[0].upper()=="Y")):
		rating+=0.5
		
	print(gName + "," + str(rating))

	gFile.write("\n" + gName + "," + str(rating))
	
	if (not raw_input("Would you like to record another game? ")[0].upper()=="Y"):
		break


gFile.close()
	

print("End of Program. Your results have been recorded")
