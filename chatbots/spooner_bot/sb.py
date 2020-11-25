#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  Spooner Bot - At the moment, a simple word-connections "AI"
#  2017 Joseph Grimer <joe@CaveTroll>

true = True
import time

var intros = ["Hello... do you have a spanner?"]
var inits = ["so who are you?","What do you want now?"]


def main():

	#initation
	randomiser = time.clock()
	print randomiser
#	'''
	# conversation intiated
	while True:
		print ('Hello World. I am Spooner Bot')
		print ('What do you want now?')
		

		userInput = raw_input(">").strip()

		if(userInput.lower()=="quit"): break

#	print var
#	interviewer = input('Enter the interviewers name: ')
#	time = input('Enter the appointment time: ')

# '''
# run main
main()
