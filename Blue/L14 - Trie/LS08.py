class Node:
    def __init__(self):
        self.stop = False
        self.child = dict()
        self.parent = None

def addNum(root, l):
    if root.stop:
        return ""
    s = ""
    tmp = root
    for i in range(1, l+1):
        next = -1
        if 0 not in tmp.child or tmp.child[0].stop == False:
            next = 0
        elif 1 not in tmp.child or tmp.child[1].stop == False:
            next = 1
        if next == -1:
            return ""
        if next not in tmp.child:
            tmp.child[next] = Node()
            tmp.child[next].parent = tmp
        s += str(next)
        tmp = tmp.child[next]
    tmp.stop = True
    while tmp.parent:
        tmp = tmp.parent
        if 0 in tmp.child and 1 in tmp.child and tmp.child[0].stop and tmp.child[1].stop:
            tmp.stop = True
    return s

n = int(input())
listNum = list(map(int, input().split()))
listNum = sorted([(listNum[i], i) for i in range(n)])
root = Node()
ans = [[] for i in range(n)]
for [l, index] in listNum:
    s = addNum(root, l)
    if s == "":
        print("NO")
        exit()
    else:
        ans[index] = s
print("YES")
for x in ans:
    print(x)