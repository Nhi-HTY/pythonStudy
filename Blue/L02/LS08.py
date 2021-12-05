n = int(input())
listClaw = list(map(int, input().split()))
count = 0
i = j = len(listClaw) - 1
while i > 0:
    j = min(j, i)
    last_kill_pos = max(0, i - listClaw[i])

    if j > last_kill_pos:
        count += (j - last_kill_pos)
        j = last_kill_pos
    i -= 1
print(n - count)



