def findSet(s):
    if parent[s] != s:
        parent[s] = findSet(parent[s])
    return parent[s]

def unionSet(a, b):
    ap = findSet(a)
    bp = findSet(b)
    if ap == bp:
        return
    parent[ap] = bp


n = int(input())
parent = [i for i in range(n + 1)]
x = []
y = []
for i in range(n):
    xi, yi = map(int, input().split())
    x.append(xi)
    y.append(yi)
for i in range(n-1):
    for j in range(i+1, n):
        if x[i] == x[j] or y[i] == y[j]:
            unionSet(i, j)

ans = 0
for i in range(n):
    if i == parent[i]:
        ans += 1
print(ans - 1)

