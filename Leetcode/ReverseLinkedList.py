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

    def reverseList(self):
        if self.head == None:
            return None
        cur = self.head
        prev = None
        while cur != None:
            nnext = cur.next
            cur.next = prev
            prev = cur
            cur = nnext
        self.head = prev

    def printList(self):
        cur = self.head
        while cur != None:
            print(cur.data, end = " ")
            cur = cur.next

list = LinkedList()
while(True):
    x = int(input())
    if(x == 0):
        break
    list.insertTail(x)

list.reverseList()
list.printList()