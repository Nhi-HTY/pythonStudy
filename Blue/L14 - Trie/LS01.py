class Node:
    def __init__(self):
        self.maxValue = -1
        self.child = dict()

def addWord(root, s, value):
    tmp = root
    for c in s:
        if c not in tmp.child:
            tmp.child[c] = Node()
        tmp = tmp.child[c]
        tmp.maxValue = max(tmp.maxValue, value)

def getMaxValue(root, s):
    tmp = root
    for c in s:
        if c not in tmp.child:
            return -1
        tmp = tmp.child[c]
    return tmp.maxValue

if __name__ == '__main__':
    n, q = map(int, input().split())
    root = Node()
    for i in range(n):
        s, w = input().split()
        addWord(root, s, int(w))

    for j in range(q):
        s = input()
        print(getMaxValue(root, s))


