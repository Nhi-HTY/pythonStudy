class Node():
    def __init__(self, x = None):
        self.data = x
        self.next = None

def isPrime(n):
    if n < 2:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
    return True

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

    def countPrime(self):
        cur = self.head
        ans = []
        while(cur != None):
            if (isPrime(cur.data)):
                ans.append(cur.data)
            cur = cur.next
        return ans

listNum = LinkedList()
ans = []
while(True):
    x = int(input())
    if x == -1:
        break
    else:
        listNum.insertTail(x)

ans = listNum.countPrime()

print(len(ans))