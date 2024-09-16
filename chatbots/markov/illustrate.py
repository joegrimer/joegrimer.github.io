import matplotlib.pyplot as plt

with open('b.json', 'r') as fo:
    all = fo.readlines()[0]

import json

numbers = json.loads(all)

plt.hist(numbers, bins=144)
plt.show()
