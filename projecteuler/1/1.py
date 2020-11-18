## Question 1 of the Euler Project

i = 3
j = 5

total = 0
total2 = 0

for x in range(0, 1000):
	if(x%3 == 0 or x%5 == 0):
		total2 = total2+x
print("totla2",total2)
	
	
while True:
	if (i >= 1000):
		break
	else:
		total = total + i
		i = i+3
		
while True:
	if (j >= 1000):
		break
	else:
		if (j%3 != 0):
			total = total + j
		j = j+5
		
print i
print j
print total
