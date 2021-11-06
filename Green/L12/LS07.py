import sys
sys.setrecursionlimit(10000)

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

    def findSecondLargest(self):
        max1 = self.head.data
        max2= -1
        cur = self.head
        while(cur != None):
            if cur.data > max1:
                max2 = max1
                max1 = cur.data
            elif cur.data < max1 and cur.data > max2:
                max2 = cur.data
            cur = cur.next
        return max2



listNum = LinkedList()
while(True):
    x = float(input())
    if x == -1:
        break
    else:
        listNum.insertTail(x)
ans = listNum.findSecondLargest()
print(ans)
