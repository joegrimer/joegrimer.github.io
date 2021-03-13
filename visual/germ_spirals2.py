from turtle import *
import time
import random

foo = 1
zoom = 100 # 1 minimum

speed(0)
while True:
    forward(int(foo/zoom))
    left(foo % 360)
    
    foo+=random.choice((1,2))
    
time.sleep(1000)
