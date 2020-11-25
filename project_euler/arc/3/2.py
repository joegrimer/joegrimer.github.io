## Question 2 of the Euler Project
'''
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

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