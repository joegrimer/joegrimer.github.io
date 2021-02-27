
preferences = {}

tops = [1,2,3,4]

i = 0
for top in tops:
    copy = top
    i+=1
    print("loop"+str(i)+"copy"+str(copy))
    while copy <= 13 and copy is not 0:
        print('subloop'+str(copy)+'<>'+str(i))
        prev_top = copy
        copy=(copy+i)%13
        if prev_top not in preferences:
            preferences[prev_top] = []
        preferences[prev_top].append(copy)


print(preferences)


