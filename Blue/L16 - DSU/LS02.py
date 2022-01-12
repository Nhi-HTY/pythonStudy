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
    elif rank[ap] > rank[bp]:
        parent[bp] = ap
    else:
        parent[ap] = bp
        rank[bp] += 1

t = int(input())
input()

for tc in range(t):
    try:
        node = input()
        rank = [0 for i in range(ord(node) + 1)]
        parent = [i for i in range(ord(node) + 1)]
        while True:
            try:
                line = input()
                if line == "":
                    break
                unionSet(ord(line[0]), ord(line[1]))
            except EOFError:
                break
        ans = 0
        for i in range(65, ord(node)+1):
            if parent[i] == i:
                ans += 1
        print(ans)
        print()
    except EOFError:
        exit()