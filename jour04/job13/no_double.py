L = [10,20,30,20,10,50,60,40,80,50,40]
L2 = []
x = 0
for nb in L:
    x += 1
for y in range(x):
    for z in range(y+1, x):
        if L[z] == L[y]:
            print(L2 = L[z])
        