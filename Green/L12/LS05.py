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

    def removeFive(self):
        prev = None
        cur = self.head
        while cur != None:
            if cur == self.head and cur.data %10 == 5:
                self.head = cur.next
                prev = cur
                cur = cur.next
            elif cur == self.tail and cur.data %10 == 5:
                    self.tail = prev
                    prev.next = None
                    cur = cur.next
            elif cur.data % 10 ==5:
                prev.next = cur.next
                cur = prev.next
            else:
                prev = cur
                cur = cur.next

    def returnArray(self):
        array = []
        cur = self.head
        while cur != None:
            array.append(cur.data)
            cur = cur.next
        return array

n = int(input())
listNum = LinkedList()
for i in range(0, n):
    x = int(input())
    listNum.insertTail(x)
listNum.removeFive()
ans = []
ans = listNum.returnArray()

for x in ans:
    print(x, end =" ")

