#!/usr/bin/python3
# a simple political simulator

from random import randint
import math

# constants
INITIAL_PEOPLE = 10
VOTING_AGE = 18

# globals
all_people = []

def random_name():
    first_names = ['Mathhew', 'Mark', 'Luke', 'John', 'Babbot','Jim','Andrew','Jarl','Karl','Charles','David','Jeremy','Theresa','Agatha','Philomina','Dominic','Thomas','Terry','Badro','Pedro','Eugine']
    last_names = ['Smith','Jones','Jerristone','Johnson',"Charl'n",'Clist','Sawyer','Boylan','Clint','Gunner','Runner','Racer','Handt']
    return first_names[randint(0,len(first_names)-1)] + ' ' + last_names[randint(0,len(last_names)-1)]

def random_age():
    return randint(1,100)

def main():

    # generate 100 people
    for i in range(0, INITIAL_PEOPLE):
        all_people.append(Person())
        print(str(all_people[-1]))

    # vote
    print('\nVoting..\n')
    for person in all_people:
        if not person.can_vote():
            continue
        voting_for = person.vote()
        print(person.name + ' votes for ' + voting_for.name)
        voting_for.votes += 1

    print('person           votes')
    for person in all_people:
        print(person.name + ' ' + str(person.age) + ' got ' + str(person.votes))

    all_people.sort(key = lambda x: x.votes)
    print('And the winner of the election is: '+str(all_people[-1]))
        
    print("End of program.")

class Person(object):
    def __init__(self):
        self.id = len(all_people)
        #all_people.append(self)
        self.income = 1000
        self.age = random_age()
        self.name = random_name()
        self.votes = 0
        self.selfish = randint(0,100) > 90
        # print('selfish?'+str(self.selfish))

    def can_vote(self):
        return self.age > 18

    def __str__(self):
        return self.name + ', ' + str(self.age) + ', ' + str(self.can_vote())
    def vote(self):
        # print('my id?'+str(self.id))
        opinions = []
        for person in all_people:
            age_proximity = abs(person.age-self.age)
            opinions.append([
                person.id,
                100-age_proximity
            ])
            opinions.sort(key = lambda x: x[1])
        if not self.selfish and opinions[-1][0] == self.id:
            return all_people[opinions[-2][0]]
        else:
            return all_people[opinions[-1][0]]

if __name__=='__main__':
    main()

