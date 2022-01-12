def findSet(s):
    if parent[s] != s:
        parent[s] = findSet(parent[s])
    return parent[s]

def unionSet(a, b):
    ap = findSet(a)
    bp = findSet(b)
    if ap == bp:
        return
    if rank[ap] < rank[bp]:
        parent[ap] = bp
        num[bp] += num[ap]
    elif rank[ap] > rank[bp]:
        parent[bp] = ap
        num[ap] += num[bp]
    else:
        parent[ap] = bp
        rank[bp] += 1
        num[bp] += num[ap]

t = int(input())

for tc in range(t):
    n, m = map(int, input().split())
    rank = [0 for i in range(n+1)]
    parent = [i for i in range(n+1)]
    num = [1 for i in range(n+1)]

    for _ in range(m):
        a, b = map(int, input().split())
        unionSet(a, b)
    ans = 0
    for i in range(n+1):
        if parent[i] == i and num[i] > ans:
            ans = num[i]
    print(ans)