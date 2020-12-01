#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  Article Digestor - At the moment, a simple word-connections "AI"
#  Copyright 2016 Joseph Grimer <joe@CaveTroll>

############################## Libraries ######################################

############################## Global Vars ####################################

############################## Main Functions #################################

def main():

	print("Welcome to Ad - son of Ai.")
	article = "John ran across the green plane. He didn't like the grass, but he loved the sun, the rain and the wind in his teeth. There was a tree at the end of the field. The tree spoke to him. The tree told him to come. The tree did not want to eat him. But he wanted to climb the tree. However, deep in the grass was hidden a snake, ready to bite those who wished to climb the tree. The tree has long curved branches. The snake was black with green stripes. You are alone. He wants to see you. The boy had red trousers, and a green shirt. The boy was ignorant. The tree was strong. The snake was malicious. The snake was actually hungry. Maybe you are hungry. Maybe this story sounds silly. It's not supposed to be art. It's just for my little experiment, you see."
#	article = "Theresa May has backed away from a pledge to require companies to put worker representatives on boards. Speaking to the CBI's annual conference, Mrs May said firms would not be forced to adopt the controversial proposal. 'This is not about mandating works councils, or the direct appointment of workers or trade union representatives on boards,' she said. Mrs May's pledge had met with a cool response from business lobby groups.The prime minister said there were 'other routes' that used existing board structures, but supplemented by advisory councils or panels. 'It will be a question of finding the model that works,' she said. Mrs May promised to shake-up corporate governance as part of her Conservative Party leadership campaign in July, and repeated the promise at last month's party conference when she said she planned to have 'not just consumers represented on company boards, but workers as well'. Asked if she had dropped plans for the direct appointment of workers on boards, Mrs May said she had 'clarified' that 'we want workers' representation on boards', but 'there are a number of ways in which that can be achieved.'She said the government would soon publish its plans to reform corporate governance, which would cover firms' accountability to shareholders, executive pay as well as proposals to ensure employees' voices were heard.In her speech to business leaders, Mrs May also pledged an extra £2bn a year in funding for scientific research and development by 2020."
	print("Article has been chosen") # (example 2 from BBC News)")

	words = article.split(" ")
	wordConnections = {}
	# the great word loop
	first = True
	last = ''
	for word in words:
		if first:
			last = word # and the last will be first :)
			first =  False
		else:
			if last in wordConnections:
				wordConnections[last].append(word)
			else:
				wordConnections[last] = [word]
			last = word

	print wordConnections
	print ("\n--------------------------------------\n")
	output = ["John"] # eventually random caps word from dict
	nextSearch = wordConnections["John"][-1]
	for i in range(0,98):
		if nextSearch in wordConnections:
			output.append(nextSearch)
#			print(wordConnections(nextSearch))
#			for each in 
			nextSearch = rollFor(wordConnections[nextSearch])
	
	print(" ".join(output)) # flush

	return 0

############################## Active Functions ###############################

randStr = 997
def rollFor(array): # randomness thing
	global randStr
	randStr+=997
#	print("raning at" + str(randStr%len(array)))
	return array[randStr%len(array)]

############################## Prep Functions #################################



if __name__ == '__main__':
	main()
















