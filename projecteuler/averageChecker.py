# Average checker - a mathematical experiment
# Joseph Grimer
# Novermber 2017

def mean(numbers):
    return sum(numbers) / len(numbers)

ages = [12,3,45,78,85,3,7,4,9,23,567,2,2,3,4,57,67,34,34,34]

print(ages)
print(ages[:-10])
print(ages[-10:])

print("The mean of the ages is>" + str(mean(ages)) + "<")

mean1=mean(ages[:-10])
print("The other mean of the ages is>" + str(mean1) + "<")
mean2=mean(ages[-10:])
print("The other mean of the ages is>" + str(mean2) + "<")

supermean = mean1 + mean2
print("supermean is" + str(mean(supermean)) )
