k = int(input())
listMonth = list(map(int, input().split()))

listMonth.sort(reverse=True)
count = 0
total = 0
if k > 0:
    for i in range(len(listMonth)):
        total += listMonth[i]
        count += 1
        if total >= k:
            break

print(-1) if total < k else print(count)