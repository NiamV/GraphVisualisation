import random
import sys

n = int(sys.argv[1])
maxWeight = int(sys.argv[2])

m = []

def weight(m):
    w = random.randint(1, 1.5*m)
    return w

for i in range(0, n):
    row = ""
    for j in range(0, n):
        w = weight(maxWeight)
        if(i == j):
            row += "MAX"
        elif(w > maxWeight):
            row += "MAX"
        else:
            row += str(w)
        row += " "
    print(row)




