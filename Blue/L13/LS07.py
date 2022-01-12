import sys
import queue
t = int(input())
def printTree(listTree, total):
    for i in range(listTree.qsize()):
        tree = listTree.get()
        print('%s %.4f' % (tree, dictName[tree] / total * 100))
try:
    input()
    for _ in range(t):
        dictName = dict()
        listName = queue.PriorityQueue()
        total = 0
        while True:
            name = input()
            if name == "":
                break
            if name not in dictName:
                dictName[name] = 1
                listName.put(name)
            else:
                dictName[name] += 1
            total += 1
        printTree(listName, total)
        if _ < t - 1:
            print()

except EOFError:
    printTree(listName, total)
    sys.exit(0)

