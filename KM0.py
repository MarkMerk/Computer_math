#!/usr/bin/env python3.9

print('Input an integer, to set the number of rows and columns in matrix')

n=int(input())

matr = [[0 for q in range(n)] for m in range(n)]

c = 0
k = 1

while c >= 0:
    i = c
    if c < n:
        while i in range(c, n-c):
            matr[c][i] = k
            k += 1
            i += 1
    else:
        break
    j= 1 + c
    if c < n:
        while j in range(c+1, n-c):
            matr[j][n-1-c] = k
            k += 1
            j += 1
    else:
        break
    m = n - 2 - c
    if c < n:
        while m in range(c, n-1-c):
            matr[n-1-c][m] = k
            k += 1
            m -= 1
    else:
        break
    b = n - 2 - c
    if c < n:
        while b in range(c+1, n-1-c):
            matr[b][0+c] = k
            k += 1
            b -= 1
    else:
        break   
    c += 1

for u in range(n):
    print(*matr[u])
