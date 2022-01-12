import queue

def BFS(graph, src, pos):
    Q = queue.Queue()
    pos[src] = 0
    Q.put(src)
    while not Q.empty():
        u = Q.get()
        for v in graph[u]:
            if pos[v] == 'undefined':
                pos[v] = pos[u] + 1
                Q.put(v)
    return pos

n = int(input())
listID = dict()
graph = []
count = 0
for _ in range(n):
    listName = input().split()
    v = []
    for name in listName:
        if name not in listID:
            id = count
            listID[name] = id
            graph.append([])
            count += 1
        else:
            id = listID[name]
        v.append(id)
    for x in v:
        for y in v:
            if x != y:
                graph[x].append(y)

pos = ['undefined' for i in range(count)]
if 'Isenbaev' in listID:
    rank = BFS(graph, listID['Isenbaev'], pos)
listName = []
for name2 in listID:
    listName.append(name2)
listName.sort()
for name3 in listName:
    print("{} {}".format(name3, pos[listID[name3]]))
