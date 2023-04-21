import random
syllables = [
"ba",
"ra",
"ta",
"cra",
"fli",
"mir",
"taw",
"fem",
"clock",
"to",
"tom",
"tof",
"tow",
"tox",
"taeog",
"daeog",
"pug",
"pewg",
"dear",
]
randSub1 = syllables[random.randint(0,len(syllables) )];
randSub2 = syllables[random.randint(0,len(syllables) )];
randSub3 = syllables[random.randint(0,len(syllables) )];
print(randSub1 + randSub2 + randSub3)
