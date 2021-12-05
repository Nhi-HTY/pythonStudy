n = int(input())
arrayN = list(map(int, input().split()))
arrayN.sort()
print(arrayN[n//2])