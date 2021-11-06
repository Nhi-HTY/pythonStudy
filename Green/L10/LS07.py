class Color():
    def __init__(self, listColor):
        self.list = listColor

    def countIndividual(self):
        result = []
        for i in range(1, 10001):
            countColor = 0
            length = 0
            eachColor = []
            for row in range(len(self.list)):
                if self.list[row][0] == i:
                    countColor +=1
                    length += self.list[row][1]
                    colorCode = self.list[row][0]
            if countColor > 0:
                eachColor.append(colorCode)
                eachColor.append(length)
                eachColor.append(countColor)
                result.append(eachColor)
        return result

n = int(input())
listColor = []

for i in range(0, n):
    color = list(map(int, input().split()))
    listColor.append(color)

result = Color(listColor).countIndividual()

print(len(result))

for row in range(len(result)):
   if row < len(result) -1:
        for col in range(0, 3):
            print(result[row][col], end =" ")
        print()
   else:
       for col in range(0, 3):
           print(result[row][col], end=" ")