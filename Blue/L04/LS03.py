import queue

def discardCards(n):
    listCards = queue.Queue()
    listDiscard = []
    for i in range(1, n+1):
        listCards.put(i)
    while listCards.qsize() > 2:
        listDiscard.append(listCards.get())
        reOrderCard = listCards.get()
        listCards.put(reOrderCard)

    if listCards.qsize() > 1:
        listDiscard.append(listCards.get())
    remainCard = listCards.get()
    if len(listDiscard) > 0:
        print("Discarded cards:", end= " ")
        for deletedCard in range(n-2):
            print(listDiscard[deletedCard], end = ", ")
        print(listDiscard[-1])
    else:
        print("Discarded cards:")
    print("Remaining card:", end = " ")
    print(remainCard)

n = int(input())
listN = []
while n > 0:
    listN.append(n)
    n = int(input())

for x in listN:
    discardCards(x)