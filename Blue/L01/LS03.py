n = int(input())
interestingMinute = list(map(int, input().split()))
ans = 0

start = 0

for i in range(len(interestingMinute)):
    gap = interestingMinute[i] - start
    if gap > 15:
        ans = start + 15
        break
    start = interestingMinute[i]

ans = start + 15
if ans >= 90:
    ans = 90
print(ans)