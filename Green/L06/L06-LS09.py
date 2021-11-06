row, column = map(int, input().split())
a_2d = []

for m in range(0, row):
    a = list(map(int, input().split()))
    a_2d.append(a)

total = 0
indies = []
for i in range(0,row):
    max = 0
    for j in range(0, column):
        if a_2d[i][j] > max:
            max = a_2d[i][j]
    for k in range(0, column):
        if a_2d[i][k] == max:
            min = 10000
            index = i
            for l in range(0, row):
                if a_2d[l][k] < min:
                    min = a_2d[l][k]
            for h in range (0, row):
                if a_2d[h][k] == min:
                    indies.append(h)
            for x in indies:
                if x == index:
                    total += 1
            indies = []

print(total)