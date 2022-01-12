class Node:
    def __init__(self, x = 0, left = None, right = None):
        self.value = x
        self.left = left
        self.right = right

    def addNode(self, x):
        if self.value > x:
            if self.left == None:
                p = Node(x)
                self.left = p
            else:
                self.left.addNode(x)
        elif self.value < x:
            if self.right == None:
                p = Node(x)
                self.right = p
            else:
                self.right.addNode(x)
        else:
            return

    def findNode(self, x):
        if self.value > x:
            if self.left != None:
                return self.left.findNode(x)
        elif self.value < x:
            if self.right != None:
                return self.right.findNode(x)
        elif self.value == x:
            return True
        return False

class BST:
    def __init__(self):
        self.root = None

    def addToBST(self, x):
        p = Node(x)
        if self.root == None:
            self.root = p
        else:
            self.root.addNode(x)

    def findBST(self, x):
        return self.root.findNode(x)

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    listStudent = list(map(int, input().split()))
    Student = BST()
    i = 0
    while i < n:
        Student.addToBST(listStudent[i])
        i += 1
    while i < (n+m):
        if Student.findBST(listStudent[i]):
            print("YES")
        else:
            print("NO")
        Student.addToBST(listStudent[i])
        i += 1

