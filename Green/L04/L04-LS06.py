def isPrime(n):
    if n < 2:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
    return True

n = int(input())
ans = 0
n1 = n
n2 = n
while (1<2):
    if isPrime(n1) == True:
        ans = n1
        print(ans)
        break
    else:
        n1 -= 1

    if isPrime(n2) == True:
        ans = n2
        print(ans)
        break
    else:
        n2 += 1



