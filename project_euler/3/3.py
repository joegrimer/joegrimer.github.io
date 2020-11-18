## Question 2 of the Euler Project
'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

'''

f = [1,1]

total = 0

while True:
	if (f[-1] > 4000000):
		break
	if (f[-1]%2==0):
		total= total+f[-1]
	f.append(f[-1]+f[-2])
		
print total
