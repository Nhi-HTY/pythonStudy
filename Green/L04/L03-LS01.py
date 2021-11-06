def isPrime(n):
    if n < 2:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
    return True

def sumPrime():
    m = int(input())
    sum = 0
    for i in range (2, m):
        if isPrime(i) == True:
            sum += i
    return sum

sum = sumPrime()
print (sum)


