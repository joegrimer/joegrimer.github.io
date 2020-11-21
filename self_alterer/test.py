#!/usr/bin/python3
import random
with open(__file__,'r') as fo:
    fc = fo.readlines()
print(fc)
newline = random.choice(fc)
splice_line = random.randrange(0,len(fc))
fc = fc[0:splice_line]+[newline]+fc[splice_line:]
with open(__file__.replace('test','testn'),'w') as fo:
    for line in fc:
        fo.write(line)
