import matplotlib.pyplot as plt

dict1 = {}

MAXD=6
MAXMAX=MAXD*MAXD*MAXD
print("maxmax", MAXMAX)

for i in range(1,MAXD+1):
    for j in range(1,MAXD+1):
        for k in range(1,MAXD+1):
            res = i*j*k
            if res not in dict1:
                dict1[res] = 0
            dict1[res] += 1

x_vars = []
y_vars = []

sum = 0
for l in range(1,MAXMAX+1):
    if l in dict1:
        x_vars.append(l)
        y_vars.append(dict1[l])


x_vars.reverse()
y_vars.reverse()

print(x_vars)
print(y_vars)

# plotting the points 
plt.plot(x_vars, y_vars, 'o', color='black')
 
# naming the x axis
plt.xlabel('summed dice result')
# naming the y axis
plt.ylabel('frequency')
 
# function to show the plot
plt.show()
