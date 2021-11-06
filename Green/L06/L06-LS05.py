def isPrime(n):
    if n < 2:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
    return True

product = 1

n = int(input())
a_2d = []
for m in range(0, n):
    a = list(map(int, input().split()))
    a_2d.append(a)


for i in range(n):
    for j in range(len(a_2d[i])):
        if j == n - 1 - i:
            if isPrime(a_2d[i][j]) == True:
                product *= a_2d[i][j]

print(product%1000003)