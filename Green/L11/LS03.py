n = int(input())
a = list(map(int, input().split()))

def isPrime(n):
    if n < 2:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
    return True

def insertAsc(a, i, x):
    j = i
    while(j>0):
        if a[j-1] <=x:
            break
        a[j] = a[j-1]
        j -=1
    a[j] = x

def insertSort(a):
    for i in range(1, len(a)):
        x = a[i]
        insertAsc(a, i, x)

b = []
for x in a:
    if isPrime(x) == False:
        b.append(x)

insertSort(b)

j =0
for i in range(len(a)):
    if isPrime(a[i]) == False:
        print(b[j], end =' ')
        j += 1
    else:
        print(a[i], end =' ')


