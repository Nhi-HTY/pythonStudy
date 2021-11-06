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
    for i in range(1, len(a)):
        x = a[i]
        insertAsc(a, i, x)

even = []
odd = []
for x in a:
    if x %2 ==0:
        even.append(x)
    else:
        odd.append(x)

insertSort(even)
insertSort(odd)

n = 0
m = len(odd)-1
for i in range(len(a)):
    if a[i] %2 ==0:
        print(even[n], end =' ')
        n += 1
    else:
        print(odd[m], end =' ')
        m -= 1


