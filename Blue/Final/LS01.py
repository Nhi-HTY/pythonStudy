n = int(input())
listNum = list(map(int, input().split()))
listNum.sort()
count = 1
for i in range(n-1):
    if listNum[i] == listNum[i+1]:
        count += 1
if count <= 2:
    print("NO")
else:
    print("YES")
    print(listNum)
    for i in range(n):
        for j in range(i, n):
            if listNum[i] == listNum[j]:
