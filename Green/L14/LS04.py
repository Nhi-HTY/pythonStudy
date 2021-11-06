class Edge():
    def __init__(self, u, v, w):
        self.u = u
        self.v = v
        self.w = w

listVertical = []
n = int(input())
for i in range(n):
    verticals = list(map(int, input().split()))
    listVertical.append(Edge(verticals[0], verticals[1], verticals[2]))

minWeight = listVertical[0].w
for u in range(1, n):
    if listVertical[u].w < minWeight:
        minWeight = listVertical[u].w

sum = 0
for j in range(n):
    if listVertical[j].w == minWeight:
        sum += listVertical[j].w
print(sum)
