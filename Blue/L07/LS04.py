import queue

class Topic:
    def __init__(self, id, oldScore, newScore):
        self.id = id
        self.oldScore = oldScore
        self.newScore = newScore
        self.change = self.newScore - self.oldScore
    def __lt__(self, other):
        return self.change > other.change or (self.change == other.change and self.id > other.id)

n = int(input())
listTopic = queue.PriorityQueue()

for _ in range(n):
    id, oldScore, post, like, comment, share = map(int, input().split())
    newScore = 0
    if post != 0:
        newScore += post * 50
    if like != 0:
        newScore += like*5
    if comment != 0:
        newScore += comment*10
    if share != 0:
        newScore += share*20
    listTopic.put(Topic(id, oldScore, newScore))

i = 0
while not listTopic.empty() and i < 5:
    value = listTopic.get()
    print("{} {}".format(value.id, value.newScore))
    i += 1
