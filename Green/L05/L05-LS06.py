def find_min(a):
    min = 1000
    for i in range(len(a)):
        if a[i] < min:
            min = a[i]
    return min

posts = int(input())
a = list(map(int, input().split()))

min = find_min(a)

energy = 0
for i in range(len(a)):
    energy += a[i] - min
print(energy)