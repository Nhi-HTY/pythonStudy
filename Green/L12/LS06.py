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
        if self.head == None:
            self.head = self.tail = p
        else:
            self.tail.next = p
            self.tail = p

    def removeHead(self):
        if self.head == self.tail:
            self.head = None
            self.tail = None
        elif self.head != None:
            self.head = self.head.next

    def returnLinkedList(self):
        cur = self.head
        while cur != None:
            print(cur.data, end = " ")
            cur = cur.next


n = int(input())
listNum = LinkedList()

for i in range(0, n):
    x, *y = map(int, input().split())
    y = y[0] if y else ''
    if x == 1:
        listNum.insertTail(y)
    if x == 0:
        listNum.removeHead()

listNum.returnLinkedList()