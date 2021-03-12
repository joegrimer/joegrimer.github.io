'''
this is supposed to be based on NN Taleb's Monte Carlo Engine

In other words, I intend to make some kind of simulation that I can "play" and acquire some kind of wisdom from.

That's very vague, I know!

Joseph Grimer - March 2021
'''

import random
import os
import datetime

def main():
    print('Welcome to my monte carlo sumilator for wisdom :P')
    options = (
        ('stranger description', five_aspects),
    )
    print('you have ' +str(len(options))+' options:')
    print('\n'.join([' '+o[0]+'\n' for o in options]), end='')
    choice = input('> ')
    options[int(choice)-1][1]()

def name_gen():
    samplenames = ('John', 'Luke', 'Klim', 'Marcus', 'Leofen','Jim','Fred','Bob','Loo Sung','Karl','Luke','Matthew','Mark','Belen', 'Alice', 'Veela', 'Lea', 'Mamli', 'Ledida', 'Jenette','Frilia','Weslu','Queen','Yaley','Ursula','Ia','Ora','Penelope')
    pairs = set(i for i in samplenames)

def five_aspects():
    sex = random.choice(('man', 'woman'))
    age = int(random.random()*100)
    traits = [random.choice(('very low','low','medium','high','very high')) for i in range(0, 5)]

    filename = str(int(datetime.datetime.now().timestamp()))+sex+str(age)+'.txt'
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
    print_to_both()
    print_to_both('name: ', random.choice(('John', 'Luke', 'Klim', 'Marcus', 'Leofen','Jim','Fred','Bob','Loo Sung','Karl','Luke','Matthew','Mark','Belen')) if sex == 'man' else \
        random.choice(('Alice', 'Veela', 'Lea', 'Mamli', 'Ledida', 'Jenette','Frilia','Weslu','Queen','Yaley','Ursula','Ia','Ora','Penelope')))
    print_to_both('born: ', random.choice(('Africa', 'England', 'Germany', 'Spain', 'France', 'South Africa', 'Blue States', 'Red States', 'Latin America', 'Brasil', 'Portugal', 'Wales','Northern Ireland','Scotland','Northumbria','Devon','Cornwall','Kent','South London','North London','Posh London')))
    print_to_both('ethnicity: ', random.choice(('black', 'white', 'east asian','middle east','tanned native','south asian')))
    print_to_both('culture:', random.choice(('Superhero Comic book', 'One punch man Anime','skateboarding','partying','reading','academic humanity','academic science','journalist science','Indie Comics','Secretarian','Self Improvement','Lobster','dinosaurs','Non Fiction','Radio 4','Voris','Heart Radio','Designer House','Designer Clothes','')))
    print_to_both('belief: ', random.choice(('None','Liberal Catholic', 'Middling Catholic', 'Traditional Catholic', 'Muslim', 'Atheist', 'Nothing Modern', 'Light Protestant', 'Protestant', 'Hindu', 'Philsoophical Secular', 'Petersonite')))
    print_to_both('job', random.choice(('manager','programmer','teacher','designer','marketing','salesman','cleaner','carer','artist','builder','fixer','accountant','secretary','mcdonalds','tesco'))
    print_to_both('family', random.choice(('alone','lives with parents','orphan','distant sibling','many cousins','parent of 1','parent of 2','parent of five','recently divorced','second marriage','lives alone. dating','lives with parents dating'))
    print_to_both('-----------------------------')
    for question in ('something said person would say: ', 'brief description: ', 'how you encounter said person: ', 'your strategy: ','what you learn: '):
        response = input(question)
        fo.write(question+response+'\n')

    fo.close()
    
    
if __name__ == '__main__':
    main()
