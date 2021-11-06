from math import sqrt

class Oxy():
    def __init__(self, mPoint, listPoints):
        self.m = mPoint
        self.l = listPoints

    def findDistance(self):
        furthest = 0
        for row in range(len(self.l)):
            distance = sqrt(pow(self.m[0] - self.l[row][0], 2) + pow(self.m[1] - self.l[row][1], 2))
            if distance > furthest:
                result = []
                furthest = distance
                result = self.l[row]
        return result

m = list(map(int, input().split()))
n = int(input())
listPoints = []
for i in range(0, n):
    point = []
    x = list(map(int, input().split()))
    point.append(x[0])
    point.append(x[1])
    listPoints.append(point)

a = Oxy(m, listPoints)
result = a.findDistance()
for x in result:
    print(x, end=" ")