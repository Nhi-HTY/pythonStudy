class Node():
    def __init__(self, x = None):
        self.data = x
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

    def insertTail(self, x):
        p = Node(x)
        if (self.head == None):
            self.head = self.tail = p
        else:
            self.tail.next = p
            self.tail = p

    def underAverage(self):
        a = self.head
        underAvg = []
        while (a != None):
            if float(a.data) < 5:
                underAvg.append(a.data)
            a = a.next
        return underAvg

listStudent = LinkedList()
ans = []

while(True):
    x = input()
    if float(x) == -1:
        break
    else:
        listStudent.insertTail(x)

ans = listStudent.underAverage()
for x in ans:
    print(x)
