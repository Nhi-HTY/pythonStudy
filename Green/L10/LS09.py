class Elements():
    def __init__(self, listSquare):
        self.list = listSquare

    def findElement(self):
        ans = []
        for row in range(len(self.list)):
            if self.list[row][2] >0:
                ans.append(self.list[row])
        return ans

m, n = map(int, input().split())
k = int(input())
listSquare = []

for i in range(0, k):
    a = list(map(int, input().split()))
    listSquare.append(a)

ans = Elements(listSquare).findElement()
print (len(ans))

for row in range(len(ans)):
    for col in range(0, 2):
        print(ans[row][col], end= " ")
    print()