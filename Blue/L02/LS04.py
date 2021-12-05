n, m, x, y = map(int, input().split())
need = list(map(int, input().split()))
available = list(map(int, input().split()))
ans = []
start1 = start2 = 0

while start1 < n and start2 < m:
    pair = []
    if need[start1] - x <= available[start2] and available[start2] <= need[start1] + y:
        pair.append(start1 + 1)
        pair.append(start2 + 1)
        ans.append(pair)
        start1 += 1
        start2 += 1
    elif available[start2] > need[start1]:
        start1 += 1
    elif available[start2] < need[start1]:
        start2 += 1

print(len(ans))
for i in range(len(ans)):
    print(ans[i][0], end = " ")
    print(ans[i][1])

