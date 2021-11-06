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

    def findEmpty(self):
        cur = self.head
        while (cur != None):
            if cur.data[2] == '0':
                print(cur.data[0], end =" ")
                print(cur.data[1])
            cur = cur.next

n = int(input())
listRoom = LinkedList()

for i in range(0, n):
    roomInfo = []
    x, y, z = list(map(str, input().split()))
    roomInfo.append(x)
    roomInfo.append(y)
    roomInfo.append(z)
    listRoom.insertTail(roomInfo)
listRoom.findEmpty()