row, column = map(int, input().split())
a_2d = []

for m in range(0, row):
    a = list(map(int, input().split()))
    a_2d.append(a)

result_2d = []

def isEven(a):
    if a % 2 == 0:
        return True

for i in range(row):
    total = 0
    for j in range(len(a_2d[i])):
        result = []
        if isEven(a_2d[i][j]) == True:
            total += 1

    result.append(i)
    result.append(total)
    result_2d.append(result)

max = 0
length = len(result_2d)
ans = 0
for k in range(length):
    if result_2d[k][1] > max:
        max = result_2d[k][1]
        ans = k
print(ans)