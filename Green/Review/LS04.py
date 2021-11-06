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

    def createList(self, listNum):
        p = Node(self.head.data)
        listNum.head = listNum.tail = p
        cur = listNum.head
        node1 = self.head
        node2 = node1.next
        while(node2 != None):
            x = node1.data + node2.data
            p = Node(x)
            listNum.tail.next = p
            listNum.tail = p
            cur = cur.next
            node1 = node1.next
            node2 = node2.next

    def printLinkedList(self, listNum):
        cur = listNum.head
        while(cur != None):
            print(cur.data, end = " ")
            cur = cur.next

listNum = LinkedList()
n = int(input())
inputNum = LinkedList()
l = list(map(int, input().split()))

for i in range(0, n):
    inputNum.insertTail(l[i])

inputNum.createList(listNum)
inputNum.printLinkedList(listNum)