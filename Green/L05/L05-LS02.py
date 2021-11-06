def find_max(a):
    max = 0
    for i in range(len(a)):
        if a[i] > max:
            max = a[i]
    print(max)

posts = int(input())
a = list(map(int, input().split()))

find_max(a)
