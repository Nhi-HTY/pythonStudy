def is_systemmaric(n):
    a = str(n)
    b = str(n)[::-1]
    return a==b

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

    def print_symmetric(self):
        cur = self.head
        i = 0
        while(cur != None):
            if (is_systemmaric(cur.data)):
                print(i, end = " ")
            cur = cur.next
            i += 1

lstNum = LinkedList()
while(True):
    x = int(input())
    if x == -1:
        break
    else:
        lstNum.insertTail(x)

lstNum.print_symmetric()