class Node:
    def __init__(self):
        self.count = 0
        self.child = dict()

def addNum(root, s):
    tmp = root
    prefixOther = False
    otherPrefix = True
    for c in s:
        if c not in tmp.child:
            tmp.child[c] = Node()
            otherPrefix = False
        tmp = tmp.child[c]
        if tmp.count == 1:
            prefixOther = True
    tmp.count = 1
    return otherPrefix + prefixOther > 0

t = int(input())

for _ in range(t):
    n = int(input())
    root = Node()
    isNotConsistent = False
    for i in range(n):
        if not isNotConsistent:
            num = input()
            isNotConsistent = addNum(root, num)
        else:
            input()
    if isNotConsistent:
        print("NO")
    else:
        print("YES")
