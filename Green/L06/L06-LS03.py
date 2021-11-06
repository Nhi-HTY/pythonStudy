def isPrime(n):
    if n < 2:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
    return True

total = 0

row, column = map(int, input().split())
a_2d = []
for m in range(0, row):
    a = list(map(int, input().split()))
    a_2d.append(a)


for j in range(0, len(a_2d[0])):
    if isPrime(a_2d[0][j]) == True:
        total += 1

for k in range(0, len(a_2d[-1])):
    if isPrime(a_2d[-1][k]) == True:
        total += 1

for l in range(1, row-1):
    if isPrime(a_2d[l][0]) == True:
        total += 1

for h in range(1, row-1):
    if isPrime(a_2d[h][column-1]) == True:
        total += 1

print(total)