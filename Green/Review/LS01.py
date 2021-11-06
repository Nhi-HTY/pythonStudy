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

    def insertFibo(self, n):
        i = 2
        prev1 = self.head
        prev2 = self.head.next
        while(i < n and n <= 10**5):
            curData = (prev1.data + prev2.data) % 1000007
            self.insertTail(curData)
            prev1 = prev1.next
            prev2 = prev2.next
            i += 1

    def printLinkedList(self):
        cur = self.head
        while(cur != None):
            print(cur.data, end= " ")
            cur = cur.next

x, y, n = list(map(int, input().split()))
listNum = LinkedList()
listNum.insertTail(x)
listNum.insertTail(y)
listNum.insertFibo(n)
listNum.printLinkedList()