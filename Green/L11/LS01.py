n = int(input())
a = list(map(int, input().split()))

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

insertSort(a)

for x in a:
    print(x, end=' ')
