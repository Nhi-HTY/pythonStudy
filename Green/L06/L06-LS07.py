row, column = map(int, input().split())
a_2d = []

for m in range(0, row):
    a = list(map(int, input().split()))
    a_2d.append(a)

total = 0

for i in range(row):
    for j in range(column):
        if a_2d[i][j] > 100:
            total +=1

print(total)
