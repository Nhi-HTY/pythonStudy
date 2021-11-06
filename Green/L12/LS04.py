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

    def insertAfter(self):
        p = Node(1)
        p.next = self.head
        self.head = p
        cur = self.head.next
        i = 2
        while cur.next != None:
            index = Node(i)
            index.next = cur.next
            cur.next = index
            cur = cur.next.next
            i +=1

    def returnArray(self):
        array = []
        cur = self.head
        while cur != None:
            array.append(cur.data)
            cur = cur.next
        return array

listNum = LinkedList()
while(True):
    x = int(input())
    if x == 0:
        break
    else:
        listNum.insertTail(x)
listNum.insertAfter()
array = listNum.returnArray()

for x in array:
    print(x, end= " ")

