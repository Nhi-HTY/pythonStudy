class Node:
    def __init__(self):
        self.count = 0
        self.child = dict()

def addWord(root, s):
    tmp = root
    global ans
    for i in range(len(s)):
        if s[i] not in tmp.child:
            tmp.child[s[i]] = Node()
        tmp = tmp.child[s[i]]
        tmp.count += 1
        ans = max(ans, tmp.count * (i+1))

t = int(input())
for tc in range(t):
    n = int(input())
    root = Node()
    ans = 0
    for i in range(n):
        dna = input()
        addWord(root, dna)
    print("Case {}: {}".format(tc+1, ans))
