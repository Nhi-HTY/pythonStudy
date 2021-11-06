listVertical = []
n = int(input())
for i in range(n):
    verticals = list(map(int, input().split()))
    listVertical.append(verticals)

adjacentList = []
for row in range(n):
    adjacent = []
    for col in range(n):
        if listVertical[row][col] == 1:
            adjacent.append(col)
    adjacentList.append(adjacent)

edgeList = []
for k in range(n):
    for x in adjacentList[k]:
        edge = []
        edge.append(k)
        edge.append(x)
        edgeList.append(edge)

print(len(edgeList))
for l in range(len(edgeList)):
    print(edgeList[l][0], end =" ")
    print(edgeList[l][1])

