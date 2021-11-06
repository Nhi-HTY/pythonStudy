listVertical = []
n, x = map(int, input().split())
for i in range(n):
    verticals = list(map(int, input().split()))
    listVertical.append(verticals)

count = 0
for i in range(n):
    if listVertical[x][i] != 0:
        count += 1

print(count)

