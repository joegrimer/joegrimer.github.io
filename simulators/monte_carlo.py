'''
this is supposed to be based on NN Taleb's Monte Carlo Engine

In other words, I intend to make some kind of simulation that I can "play" and acquire some kind of wisdom from.

That's very vague, I know!

Joseph Grimer - March 2021
'''

import random
import os

def main():
    print('welcome to my monte carlo sumilator for wisdom :P')
    options = (
        ('five aspects', five_aspects),
    )
    print('you have ' +str(len(options))+' options:')
    print('\n'.join([' '+o[0]+'\n' for o in options]), end='')
    choice = input('> ')
    options[int(choice)-1][1]()

def five_aspects():
    sex = random.choice(('man', 'woman'))
    age = int(random.random()*100)
    traits = [int(random.random()*100) for i in range(0, 5)]

    filename = '-'.join([str(i) for i in traits])+' '+sex+' '+str(age)+'.txt'
    if not os.path.exists('people'):
        os.mkdir('people')

    fo = open('people/' + filename, 'w+')

    def print_to_both(*args):
        fo.write(' '.join([str(i) for i in args])+'\n')
        print(*args)

    print_to_both('person')

    print_to_both('sex\t\t', sex)
    print_to_both('age\t\t', age)
    print_to_both()
    print_to_both('assertiveness\t\t', traits[0])
    print_to_both('neuroticism\t\t', traits[1])
    print_to_both('concienciousness\t', traits[2])
    print_to_both('extraversion\t\t', traits[3])
    print_to_both('openness to experience\t', traits[4])

    print_to_both('name: ', random.choice(('John', 'Luke', 'Klim', 'Marcus', 'Leofen')) if sex == 'man' else random.choice(('Alice', 'Veela', 'Lea', 'Mamli', 'Ledida', 'Jenette')))
    print_to_both('ethnicity: ', random.choice(('African Black', 'English white', 'German white', 'SPanish white', 'French Black', 'South African White')))
    print_to_both('culture:', random.choice(('Superhero Comic book', 'One punch man Anime')))
    print_to_both('belief: ', random.choice(('Liberal Catholic', 'Middling Catholic', 'Traditional Catholic', 'Muslim', 'Atheist', 'Nothing Modern', 'Light Protestant', 'Protestant', 'Hindu', 'Philsoophical Secular', 'Petersonite')))
    
    print_to_both('-----------------------------')
    response = input('your description: ')
    fo.write('your description: '+desc)
    response = input('how you encounter said person: ')
    fo.write('your encounter: '+response)
    response = input('your strategy: ')
    fo.write('your response: '+response)
    response = input('what you learn: ')
    fo.write('what you learn: '+response)

    fo.close()
    
    
if __name__ == '__main__':
    main()
