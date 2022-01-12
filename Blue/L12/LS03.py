n, m = map(int, input().split())
line = list(map(int, input().split()))
line.sort()
l = 0
r = line[-1]
mid = 0
res = 0
while l <= r:
    cut = 0
    mid = int((l+r) // 2)
    for i in range(n):
        if line[i] > mid:
            cut += line[i] - mid
    if cut >= m:
        l = mid + 1
        res = mid
    elif cut < m:
        r = mid - 1
print(res)