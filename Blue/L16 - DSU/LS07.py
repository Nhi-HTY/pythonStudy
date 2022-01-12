import queue

class Node:
    def __init__(self):
        self.data = value

    def __lt__(self, other):
        self.data <= other.data

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

n, q = map(int, input().split())
rank = [0 for i in range(n + 1)]
parent = [i for i in range(n + 1)]
num = queue.PriorityQueue()
qNode = dict()

for i in range(n+1):
    qNode[i] = i
for j in range(n+1):
    num.put(Node())
for _ in range(q):
    a, b = map(int, input().split())
    unionSet(a, b)
