fre_x = [False] * (10 ** 6 + 5)
fre_y = [False] * (10 ** 6 + 5)
x_unique = []
y_unique = []
i = 0
points = []
while i < 8:
    x, y = map(int, input().split())
    points.append((x, y))

    if not fre_x[x]:
        fre_x[x] = True
        x_unique.append(x)

    if not fre_y[y]:
        fre_y[y] = True
        y_unique.append(y)
    i += 1

x_unique.sort()
y_unique.sort()
points.sort()
index = 0
if len(x_unique) == 3 and len(y_unique) == 3:
    for i in range(3):
        for j in range(3):
            if i == j == 1:
                continue
            if x_unique[i] == points[index][0] and y_unique[j] == points[index][1]:
                index += 1
            else:
                print('ugly')
                exit()
    print('respectable')
else:
    print("ugly")