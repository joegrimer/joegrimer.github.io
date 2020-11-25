import re

whatonary={
    "john":"the man upstairs",
    "jeeves":"the man downstairs",
    "a calculator":"a computational device",
    "a mug":"a ceramic container of liquid",
    "a cow":"a farm animal that makes a moo sound",
    "a fish":"a creature that can swim",
}
def main():

    ask("hello there!")
    ask("What is your name")
    #person = input('Enter your name: ')
    #print('Hello', person)
    question = input('What would you like to know?')
    parseQuestion(question)

def parseQuestion(question):
#    print("lala")
#m = re.search('(?<=abc)def', 'abcdef')
    while(true):
        if ( re.search(question.lower(),"what is") ):
            pred=question.lower().split("what is ")[1]
            print(pred +" is " + dictionary[pred])
        else:
            print("I am sorry. My ignorance is shown by my inability to know what the heck you are talking about.")
            print("please tell me the answer")

def ask(question):
    answer = input("R: " + question + "?\n H: ")
    return answer

def say(sentence):
    print("R: " + sentence)

def humanSpeak(sentence):
    print("H: " + sentence)

#run main
main()
