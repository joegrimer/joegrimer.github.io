# import random
import matplotlib.pyplot as plt

MAX_RANGE = 144
RRANGE = 99999

numbers = []


for i in range(1, MAX_RANGE):
    for j in range(1, MAX_RANGE):
        numbers.append(
            i*j
        )

plt.hist(numbers, bins=MAX_RANGE)
plt.show()

numbers = []
print("normal")

for i in range(1, RRANGE):
    numbers.append(i)
    # numbers.append(random.randint(1, MAX_RANGE))

plt.hist(numbers, bins=MAX_RANGE)
plt.show()

#print("now with max")

#numbers = []
#for i in range(1, RRANGE):
    #numbers.append(max((
    #    random.randint(1, MAX_RANGE),
    #    random.randint(1, MAX_RANGE),
    #    ))
    #)

#plt.hist(numbers, bins=MAX_RANGE)
#plt.show()

print("now squared")
