n = int(input())
button = list(map(int, input().split()))

count = 0
for i in range(len(button)):
    if button[i] == 1:
        count += 1
flag = True
if len(button) == 1 and count < len(button):
    flag = False

elif len(button) > 1 and (count < len(button) - 1 or count == len(button)):
    flag = False

print("YES") if flag == True else print("NO")

