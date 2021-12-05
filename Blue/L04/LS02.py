def canReorder(listCar, n):
    sortedListCar = []
    for x in listCar:
        sortedListCar.append(x)
    sortedListCar.sort()
    sideStreet = []
    ans = []
    j = 0
    i = 0
    while i < n:
        if len(sideStreet) > 0 and len(ans) > 0:
            if sideStreet[-1] == ans[-1] + 1:
                ans.append(sideStreet[-1])
                sideStreet.pop()
                j += 1
                continue
        if listCar[i] > sortedListCar[j] and j < n-1:
            sideStreet.append(listCar[i])
            i += 1
        else:
            ans.append(listCar[i])
            i += 1
            j += 1
    for x in range(len(sideStreet)):
        ans.append(sideStreet.pop())
    flag = True
    for k in range(n):
        if sortedListCar[k] != ans[k]:
            flag = False
    print("yes") if flag == True else print("no")

n = int(input())
listCar = []
listN = []
listN.append(n)
while n > 0:
    car = list(map(int, input().split()))
    listCar.append(car)
    n = int(input())
    listN.append(n)

i = 0
while listN[i] > 0:
    canReorder(listCar[i], listN[i])
    i += 1


