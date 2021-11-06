import sys
sys.setrecursionlimit(10000000)
array = []

class Node():
    def __init__(self, x = 0, left = None, right = None):
        self.data = x
        self.left = left
        self.right = right

    def addToNode(self, x):
        if x < self.data:
            if self.left == None:
                p = Node(x)
                self.left = p
            else:
                self.left.addToNode(x)
        if x > self.data:
            if self.right == None:
                p = Node(x)
                self.right = p
            else:
                self.right.addToNode(x)

    def printSumNode(self, x):
        if self.left != None:
            self.left.printSumNode(x)
        if self.right != None:
            self.right.printSumNode(x)
        if self.data < x:
            array.append(self.data)

class BST():
    def __init__(self):
        self.root = None

    def addToBST(self, x):
        p = Node(x)
        if self.root == None:
            self.root = p
        else:
            self.root.addToNode(x)

    def printSumBST(self, x):
        self.root.printSumNode(x)

listNum = BST()
n, x = map(int, input().split())
inputNum = list(map(int, input().split()))
for i in range(n):
    listNum.addToBST(inputNum[i])

listNum.printSumBST(x)
ans = 0
for i in array:
    ans += i
print(ans)