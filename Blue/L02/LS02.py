n, m = map(int, input().split())
listProblems = list(map(int, input().split()))
listGeorgePrepare = list(map(int, input().split()))

start1 = start2 = 0
prepare = 0

while start1 < n and start2 < m:
    if listProblems[start1] <= listGeorgePrepare[start2]:
        start1 +=1
        start2 += 1
        prepare +=1
    else:
        start2 += 1

print(n-prepare)