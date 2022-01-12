import math

n, s = map(int, input().split())
listR = dict()
R = []
for _ in range(n):
    x, y, population = map(int, input().split())
    r2 = x*x + y*y
    if r2 in listR:
        listR[r2] += population
    else:
        listR[r2] = population
for r in listR:
    R.append(r)
R.sort()
for i in R:
    s += listR[i]
    if s >= 1000000:
        print(math.sqrt(i))
        exit()
print("-1")
