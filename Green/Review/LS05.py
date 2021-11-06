import sys
sys.setrecursionlimit(10000000)

def isSymmetric(input, i, j):
    if i > j:
        return True
    if input[i] == input[j]:
        return isSymmetric(input, i+1, j-1)
    return False

n = int(input())
inputString = input()
if(isSymmetric(inputString, 0, n-1) == True):
    print("YES")
else:
    print("NO")