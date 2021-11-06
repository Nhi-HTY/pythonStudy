from math import sqrt

class Triagle():
    def __init__(self, listTriagle):
        self.list = listTriagle

    def calculateArea(self):
        totalArea = 0
        for i in range(0, len(self.list), 3):
            distance12 = sqrt(pow(self.list[i][0] - self.list[i+1][0], 2) + pow(self.list[i][1] - self.list[i+1][1], 2))
            distance13 = sqrt(pow(self.list[i][0] - self.list[i+2][0], 2) + pow(self.list[i][1] - self.list[i+2][1], 2))
            distance23 = sqrt(pow(self.list[i+1][0] - self.list[i+2][0], 2) + pow(self.list[i+1][1] - self.list[i+2][1], 2))
            s = (distance12 + distance13 + distance23)/2
            area = sqrt(s*(s-distance12)*(s-distance13)*(s-distance23))
            totalArea += area
        return totalArea

n = int(input())
listTriagle = []

for i in range(0, n):
    firstPoint = list(map(int, input().split()))
    secondPoint = list(map(int, input().split()))
    thirdPoint = list(map(int, input().split()))
    listTriagle.append(firstPoint)
    listTriagle.append(secondPoint)
    listTriagle.append(thirdPoint)

result = Triagle(listTriagle).calculateArea()

print("{:.2f}".format(result))