#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  gg.py - Go game - a python AI implementation of Go
#  
#  Copyright 2016 Joseph Grimer <joe@CaveTroll>
#  

#import time
#time.sleep(5) # delays for 5 seconds

'''
Notes:
1 is Black
2 is White
'''
### Globals

Empty = 0
Black = 1
White = 2
boardSize=5

### Main Function

def main():

	print("\nWelcome to my Go Simulator\n---\nJoseph Grimer 2017\n")
	ban=prepareGoban()
	turn=Black
	print("Board Prepared; Simulation starting...\n")

	while True:
		playAt(rand(availableSpaces(ban)),ban,turn)
		turn = nextTurn(turn)
#		print turn
		playAt([2,4],ban,turn)
		turn = nextTurn(turn)
		playAt([4,4],ban,turn)
		turn = nextTurn(turn)
		break

	print "End of Simulation. Final board state:\n"
	printBan(ban)
	
def rand(ary):
	response = ary[0]
	return response

def availableSpaces(ban):
	blanks=[]
	for x in ban:
		for y in x:
			if y==Empty:
				blanks.append([x,y])
	return blanks

def	playAt(coords,ban,turn):
	x=coords[0]
	y=coords[1]
	if ban[x][y]==Empty:
		ban[x][y]=turn
	else:
		print "Error: Somebody tried to play on top of a stone at "+str(x)+"-"+str(y)+". It didn't work out...\n"
		return False
	
def nextTurn(turn):
	if turn==Black:
		turn=White
	elif turn==White:
		turn=Black
	else:
		print "Apparently, it's nobody's turn! Nooooo...!"
	return turn

def prepareGoban(): # goban is go ban in japanise, I think
	goban = []
	for x in range(boardSize):
		line=[]
		for y in range(boardSize):
			line.append(Empty)
		goban.append(line)
	return goban

def printBan(ban): #idea: make this print multiple gobans horizontally
	edge='+'
	middle=''
	for i in ban:
		middle+="|"
		edge+="-"
		for j in i:
			if j==Black:
				middle+="0"
			elif j==White:
				middle+="O"
			else:
				middle+=" "
		middle+="|\n"
	edge += '+\n'
	print edge+middle+edge

if __name__ == '__main__':
	main()
