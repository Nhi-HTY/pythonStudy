posts = int(input())
a = list(map(int, input().split()))
count = 0
for i in range(len(a)):
    count += a[i]
print(count)