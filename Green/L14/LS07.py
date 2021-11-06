listVertical = []
listWeight = []
n, k = map(int, input().split())

def insertAsc(a, i, x):
    j = i
    while(j>0):
        if a[j-1] <=x:
            break
        a[j] = a[j-1]
        j -=1
    a[j] = x

def insertSort(a):
    for i in range(1, n):
        x = a[i]
        insertAsc(a, i, x)

for i in range(n):
    verticals = list(map(int, input().split()))
    listVertical.append(verticals)
    listWeight.append(verticals[2])

insertSort(listWeight)

while(k>0):
    j = k-1
    for u in range(n):
        if listVertical[u][2] == listWeight[j]:
            print(listVertical[u][0], end = " ")
            print(listVertical[u][1])
            break
    k -= 1

