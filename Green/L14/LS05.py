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

count = 0
product = 1
for j in range(n):
    if listVertical[j].u == listVertical[j].v:
        count +=1
        product *= listVertical[j].w

if count < 1:
    print(-1)
else:
    print(count, end = " ")
    print(product % (10**6 + 7))
