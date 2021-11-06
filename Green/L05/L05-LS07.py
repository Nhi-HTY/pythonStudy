n = int(input())
a = list(map(int, input().split()))

total_boy = 0
total_girl = 0
for i in range(len(a)):
    if a[i] == 0:
        total_boy += 1
    else:
        total_girl +=1
if (total_boy == total_girl):
    print("YES")
else:
    print("NO")