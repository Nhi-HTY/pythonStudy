class Node:
    def __init__(self):
        self.stop = 0
        self.child = dict()

def addWord(root, s):
    tmp = root
    for c in s:
        if c not in tmp.child:
            tmp.child[c] = Node()
        elif tmp.child[c].stop == 1:
            return False
        tmp = tmp.child[c]
    tmp.stop += 1
    return len(tmp.child) == 0

if __name__ == '__main__':
    n = int(input())
    root = Node()
    for _ in range(n):
        line = input()
        isNotVulnerable = addWord(root, line)
        if not isNotVulnerable:
            print("vulnerable")
            exit()
    print("non vulnerable")
