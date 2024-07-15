#!/usr/bin/python
from random import randint

lines = ()
try:
    with open('/Users/joseph.grimer/.rolls.txt', 'r') as fo:
        lines = fo.readlines()
except:
    pass

with open('/Users/joseph.grimer/.rolls.txt', 'a+') as fo:
    for _ in range(0, len(lines)+1):
        newline = str(randint(1,6)) + ' ' + str(randint(1,6)) + ' ' + str(randint(1,6))
        fo.write(newline+' and ')
        print(newline)
    fo.write('\n')
