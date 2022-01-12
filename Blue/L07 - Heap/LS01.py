import queue

class Reverse:
    def __init__(self, value):
        self.value = value
    def __lt__(self, other):
        return self.value > other.value

n = int(input())
a = list(map(int, input().split()))
pq = queue.PriorityQueue()

for i in range(n):
    pq.put(Reverse(a[i]))

    if i < 2:
        print(-1)
    else:
        first = pq.get()
        second = pq.get()
        third = pq.get()

        print(first.value * second.value * third.value)

        pq.put(Reverse(first.value))
        pq.put(Reverse(second.value))
        pq.put(Reverse(third.value))