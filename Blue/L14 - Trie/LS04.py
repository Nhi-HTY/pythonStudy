class Node:
    def __init__(self):
        self.countWord = 0
        self.child = dict()

def addNode(root, s):
    tmp = root
    for c in s:
        if c not in tmp.child:
            tmp.child[c] = Node()
        tmp.child[c].countWord += 1
        tmp = tmp.child[c]

def findNode(root, s):
    tmp = root
    for c in s:
        if c not in tmp.child:
            return 0
        tmp = tmp.child[c]
    return tmp.countWord

n = int(input())
root = Node()
for _ in range(n):
    line = input().split()
    if line[0] == "add":
        addNode(root, line[1])
    elif line[0] =="find":
        print(findNode(root, line[1]))
