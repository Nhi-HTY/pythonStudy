listVertical = []
flag = True

n = int(input())
for i in range(n):
    verticals = list(map(int, input().split()))
    listVertical.append(verticals)

for row in range(n):
    count = 0
    for col in range(n):
        if listVertical[row][col] == 1:
            count += 1
    if count % 2 != 0:
        flag = False

if (flag == True):
    print("YES")
else:
    print("NO")



