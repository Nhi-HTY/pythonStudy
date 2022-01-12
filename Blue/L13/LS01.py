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
                listDistinct.append(x)
            else:
                self.left.addNode(x)
        elif self.value < x:
            if self.right == None:
                p = Node(x)
                self.right = p
                listDistinct.append(x)
            else:
                self.right.addNode(x)
        else:
            return

class BST:
    def __init__(self):
        self.root = None

    def addToBST(self, x):
        p = Node(x)
        if self.root == None:
            self.root = p
            listDistinct.append(x)
        else:
            self.root.addNode(x)

t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    listDistinct = []
    listNum = BST()
    for i in range(n):
        listNum.addToBST(a[i])
    l = len(listDistinct)
    if l == x:
        print("Good")
    elif l > x:
        print("Average")
    else:
        print("Bad")

