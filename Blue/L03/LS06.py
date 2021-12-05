totalBar = int(input())
listBar = list(map(int, input().split()))

listBar.sort()
totalTower = height = maxHeigth = 1

for i in range(1, totalBar):
    if listBar[i] == listBar[i-1]:
        height += 1
    else:
        height = 1
        totalTower += 1
    maxHeigth = max(maxHeigth, height)

print(maxHeigth, end = " ")
print(totalTower)
