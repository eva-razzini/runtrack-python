L = [10,5,9,1,3,7]
x = 0
for nb in L:
    x += 1
for y in range(x):
    for z in range(y+1, x):
        if L[z] < L[y]:
            L[y], L[z] = L[z], L[y]
print(L)