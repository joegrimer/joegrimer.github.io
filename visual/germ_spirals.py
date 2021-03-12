from turtle import *
import time

foo = 1
zoom = 400 # 1 minimum

speed(0)
while True:
    forward(int(foo/zoom))
    right(foo % 360)
    
    foo+=1
    
time.sleep(1000)
