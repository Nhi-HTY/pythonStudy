dictS = dict()

class Node:
    def __init__(self, x = 0, left = None, right = None):
        self.order = x
        self.left = left
        self.right = right

    def addNode(self, x):
        if self.order > x:
            if self.left == None:
                p = Node(x)
                self.left = p
                if x not in dictS:
                    dictS[x] = 1
            else:
                self.left.addNode(x)
        elif self.order < x:
            if self.right == None:
                p = Node(x)
                self.right = p
                if x not in dictS:
                    dictS[x] = 1
            else:
                self.right.addNode(x)
        if self.order == x:
            if x in dictS:
                dictS[x] += 1

class BST:
    def __init__(self):
        self.root = None

    def addToBST(self, x):
        p = Node(x)
        if self.root == None:
            self.root = p
            if x not in dictS:
                dictS[x] = 1
        else:
            self.root.addNode(x)

s = input()
t = input()
yay = 0
woops = 0
listS = BST()
for i in range(len(s)):
    listS.addToBST(ord(s[i]))
for x in t:
    if ord(x) in dictS:
        yay += 1
        dictS[ord(x)] -= 1
for k in t:
    if ord(k) >= 97:
        char = ord(k) - 32
        if char in dictS and dictS[char] > 0:
            woops += 1
            dictS[char] -= 1
    else:
        char = ord(k) + 32
        if char in dictS and dictS[char] > 0:
            woops += 1
            dictS[char] -= 1
print(yay, woops)

