def isPrime(n):
    if n < 2:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
    return True

posts = int(input())
a = list(map(int, input().split()))

count = 0
for i in range(len(a)):
    if isPrime(a[i]) == True:
        count += 1
print(count)