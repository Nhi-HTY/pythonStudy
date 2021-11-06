def find_like(a):
    len(a)
    for i in range(len(a)):
        if a[i] == 0:
            return False
            break

posts = int(input())
a = list(map(int, input().split()))

result = find_like(a)

if result == False:
    print("NO")
else:
    print("YES")