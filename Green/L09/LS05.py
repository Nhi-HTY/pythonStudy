a = int(input())

if a < 0:
    n = a * (-1)
else:
    n = a

def findMax(n):
    last = n%10
    rest = n//10
    if (rest == 0):
        return last
    else:
        maxDigit = findMax(rest)
        if maxDigit > last:
            return maxDigit
        else:
            return last

print(findMax(n))