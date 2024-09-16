# import random
import matplotlib.pyplot as plt

MAX_RANGE = 144

numbers = []

for i in range(1, MAX_RANGE):
    for j in range(1, MAX_RANGE):
        numbers.append(
            max((i, j))
        )

plt.hist(numbers, bins=250)
plt.show()
