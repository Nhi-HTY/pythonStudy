class Node():
    def __init__(self, x = 0, left = None, right = None):
        self.data = x
        self.left = left
        self.right = right

    def insertNode(self, x):
        p = Node(x)
        if self.left == None:
            self.left = p
        elif self.right == None:
            self.right = p
        else:
            self.left.insertNode(x)



    def inoderTraversalNode(self):
        if self.left != None or self.left.val != "null":
            self.left.inoderTraversalNode()
        else:
            print(self.data)
            if self.right != None:
                self.right.inoderTraversalNode()

class BST():
    def __init__(self):
        self.root = None

    def insertBST(self, x):
        p = Node(x)
        if self.root == None:
            self.root = p
        else:
            self.root.insertNode(x)

    def inorderTraversalBST(self):
        self.root.inoderTraversalNode()



listNum = BST()
n = int(input())
a = list(map(str, input().split()))

i = 0
while i < n:
    for j in range(i, i+2):
        while j < n:
            listNum.insertBST(int(a[j]))
    i += 2

listNum.inorderTraversalBST()
    
