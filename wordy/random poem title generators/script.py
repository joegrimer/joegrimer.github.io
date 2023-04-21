import random
subjects = [
"The Flower",
"The Watch",
"The Pot",
"The Pen",
"The Paper",
"The Sphere",
"The Glasses",
"The Cards",
]
predicates = [
" is green",
" is yellow",
" was red",
" was blue",
" was white",
" was black",
" will be white",
]
randSub = subjects[random.randint(0,len(subjects) )];
randPred = predicates[random.randint(0,len(predicates) )];
print(randSub + randPred)
