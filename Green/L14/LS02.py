listVertical = []
n = int(input())
for i in range(n):
    verticals = list(map(int, input().split()))
    listVertical.append(verticals)

flag = True
edgeList = []
for u in range(n):
    for v in range(n):
        if listVertical[u][v] != listVertical[v][u]:
            flag = False
            break

if flag == True:
    print("YES")
else:
    print("NO")


