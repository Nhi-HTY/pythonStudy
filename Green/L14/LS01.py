class Edge():
    def __init__(self, u, v):
        self.u = u
        self.v = v

listVertical = []
n = int(input())
for i in range(n):
    verticals = list(map(int, input().split()))
    listVertical.append(verticals)

edgeList = []
for u in range(n):
    for v in range(n):
        if listVertical[u][v] == 1 and u < v:
            edgeList.append(Edge(u, v))

length = len((edgeList))
print(length)
for j in range(length):
    print(edgeList[j].u, end = " ")
    print(edgeList[j].v)


