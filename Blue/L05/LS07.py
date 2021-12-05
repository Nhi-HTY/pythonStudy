import queue

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

class Cell:
    def __init__(self, r, c):
        self.r = r
        self.c = c

def isInMatrix(u, v, m, n):
    return 0 <= u < m and 0 <=v < n

def BFS(start):
    q = queue.Queue()
    q.put(start)

    while q.qsize() > 0:
        u = q.get()
        for i in range(4):
            row = u.r + dx[i]
            column = u.c + dy[i]
            if row == end.r and column == end.c and listIce[row][column] == "X":
                return True
            if isInMatrix(row, column, n, m) and listIce[row][column] == ".":
                q.put(Cell(row, column))
                listIce[row][column] = "X"
    return False


n, m = map(int, input().split())
listIce = [None] * 1000
for i in range(n):
    listIce[i] = list(input())
s1, s2 = map(int, input().split())
start = Cell(s1-1, s2-1)
e1, e2 = map(int, input().split())
end = Cell(e1-1, e2-1)

print("YES") if BFS(start) == True else print ("NO")

# from queue import Queue
#
# dr = [0, 0, -1, 1]
# dc = [1, -1, 0, 0]
#
# MAX = 500 + 1
# level = [None] * MAX
#
# def BFS(sr, sc, fr, fc):
#     q = Queue()
#     q.put((sr, sc))
#     level[sr][sc] = 'X'
#
#     while q.qsize() > 0:
#         ur, uc = q.get()
#
#         for i in range(4):
#             r = ur + dr[i]
#             c = uc + dc[i]
#
#             if r == fr and c == fc and level[r][c] == 'X':
#                 return True
#
#             if r in range(n) and c in range(m) and level[r][c] == '.':
#                 level[r][c] = 'X'
#                 q.put((r, c))
#
#     return False
#
# n, m = map(int, input().split())
#
# for i in range(n):
#     level[i] = list(input())
#
# sr, sc = map(int, input().split())
# fr, fc = map(int, input().split())
#
# print("YES" if BFS(sr - 1, sc - 1, fr - 1, fc - 1) else "NO")