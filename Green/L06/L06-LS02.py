row, column = map(int, input().split())

a_2d = []
for m in range(0, row):
    a = list(map(int, input().split()))
    a_2d.append(a)

result = []

for i in range(0, column):
    flag = True
    for j in range(0, row):
        if (a_2d[j][i] >= 0):
            flag = False
            break
    if flag == True:
        result.append(i)

for x in result:
    print(x, end =" ")
