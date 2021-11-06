a = int(input())

if a < 0:
    n = a * (-1)
else:
    n = a

def findFirst(n):
    if n < 10:
        return n
    return findFirst(n//10)

print(findFirst(n))