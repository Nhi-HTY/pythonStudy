import sys
sys.setrecursionlimit(10000000)

class Node():
    def __init__(self, x = 0, left = None, right = None):
        self.data = x
        self.left = left
        self.right = right

    def addToNode(self, x):
        if (x < self.data):
            if (self.left == None):
                p = Node(x)
                self.left = p
            else:
                self.left.addToNode(x)
        if (x > self.data):
            if (self.right == None):
                p = Node(x)
                self.right = p
            else:
                self.right.addToNode(x)
        else:
            return

    def minNode(self):
        if self.left == None:
            return self.data
        else:
            return self.left.minNode()


class BST():
    def __init__(self):
        self.root = None

    def addToBST(self, x):
        p = Node(x)
        if (self.root == None):
            self.root = p
        else:
            self.root.addToNode(x)

    def minBST(self):
        return self.root.minNode()

listNum = BST()
n = int(input())
a = list(map(int, input().split()))

for i in range(n):
    listNum.addToBST(a[i])

ans = listNum.minBST()
print(ans)


