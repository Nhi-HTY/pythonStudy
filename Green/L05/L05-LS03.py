def find_even(a):
    for i in range(len(a)):
        if a[i] % 2 ==0:
            print(a[i])

posts = int(input())
a = list(map(int, input().split()))

find_even(a)
