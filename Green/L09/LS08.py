import sys
sys.setrecursionlimit(10000)

n = int(input())
binary = []
def findBinary(n):
    if n == 0:
        remainder = 0
    elif n == 1:
        remainder = 1
    else:
        findBinary(n//2)
        remainder = n % 2
    binary.append(remainder)

findBinary(n)
for x in binary:
    print("{}".format(x), end='')