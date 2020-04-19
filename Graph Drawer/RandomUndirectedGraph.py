import random
import sys

n = int(sys.argv[1])
maxWeight = int(sys.argv[2])

m = [[0 for i in range(0, n)] for j in range(0, n)]

def weight(m, n):
    r = random.random()
    k = (m / ((1 - m**0.5)**2)) * (3 / n)**2
    d = 1 - (k**0.5) 
    if r < ( (n-3) / n):
        w = m + 1
    else:
        w = (k / ((r-d) ** 2))

    return int(w)

for i in range(0, n):
    for j in range(0, n):
        w = weight(maxWeight, n)
        if(i == j):
            m[i][j] = "MAX"
            m[j][i] = "MAX"
        elif(w > maxWeight):
            m[i][j] = "MAX"
            m[j][i] = "MAX"
        else:
            m[i][j] = str(w)
            m[j][i] = str(w)

for row in m:
    r = ""
    for elem in row:
        r += elem
        r += " "
    print(r)

    
