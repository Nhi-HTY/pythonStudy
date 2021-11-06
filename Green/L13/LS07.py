import sys
sys.setrecursionlimit(10000000)

class Student():
    def __init__(self, studenID, name, grade):
        self.id = studenID
        self.name = name
        self.grade = grade

    def __str__(self):
        return self.id + " " + self.name + " " + str(self.grade)

class Node():
    def __init__(self, x = 0, left = None, right = None):
        self.data = x
        self.left = left
        self.right = right

    def addToNode(self, x):
        if x.grade < self.data.grade:
            if self.left == None:
                p = Node(x)
                self.left = p
            else:
                self.left.addToNode(x)
        if x.grade > self.data.grade:
            if self.right == None:
                p = Node(x)
                self.right = p
            else:
                self.right.addToNode(x)
        else:
            return

    def printHighestNode(self):
        if self.right != None:
            self.right.printHighestNode()
        else:
            print(self.data)


class BST():
    def __init__(self):
        self.root = None

    def addToBST(self, x):
        p = Node(x)
        if self.root == None:
            self.root = p
        else:
            self.root.addToNode(x)

    def printHighestBST(self):
        self.root.printHighestNode()

listNum = BST()
n = int(input())
for i in range(n):
    studentID, name, grade = list(map(str, input().split()))
    listNum.addToBST(Student(studentID, name, float(grade)))

listNum.printHighestBST()



