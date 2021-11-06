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

    def lastestDate(self):
        if self.head == None:
            return None

        cur = self.head
        latest = cur
        cur = cur.next

        while cur:
            if cur.data.isNewer(latest.data):
                latest = cur
            cur = cur.next
        return latest

class Date():
    def __init__(self, day = 0, month = 0, year = 0):
        self.day = day
        self.month = month
        self.year = year

    def isNewer(self, other):
        return self.year > other.year or (self.year == other.year and (self.month > other.month or (self.month == other.month and self.day > other.day)))

    def __str__(self):
        return str(self.day) + " " + str(self.month) + " " + str(self.year)

listDate = LinkedList()
n = int(input())
for i in range(n):
    date, month, year = list(map(int, input().split()))
    listDate.insertTail(Date(date, month, year))

ans = listDate.lastestDate()
if ans:
    print(ans.data)
else:
    print(0)

