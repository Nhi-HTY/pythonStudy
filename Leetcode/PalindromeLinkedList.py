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

    def isPalindrome(self):
        duplicatedLinkedList = self.dupLinkedList()
        reverseHead = self.reverseLinkedList(duplicatedLinkedList.head)
        cur1 = self.head
        cur2 = reverseHead
        while (cur1 is not None):
            if cur1.data != cur2.data:
                return False
            cur1 = cur1.next
            cur2 = cur2.next
        return True

    def dupLinkedList(self):
        cur = self.head
        linkedList2 = LinkedList()
        linkedList2.insertTail(cur.data)
        cur = cur.next
        while (cur is not None):
            linkedList2.insertTail(cur.data)
            cur = cur.next
        return linkedList2

    def reverseLinkedList(self, head):
        cur = head
        prev = None

        while (cur is not None):
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
            head = prev
        return head

list = LinkedList()
while(True):
    x = int(input())
    if(x == 0):
        break
    list.insertTail(x)

result = list.isPalindrome()
print(result)