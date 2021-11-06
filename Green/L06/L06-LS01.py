row, column = map(int, input().split())

a_2d = []
for i in range(0, row):
    a = list(map(int, input().split()))
    a_2d.append(a)

for j in range(len(a_2d)):
    sum = 0
    for m in range(len(a_2d[j])):
        sum += a_2d[j][m]
    print("{}: {}".format(j, sum))