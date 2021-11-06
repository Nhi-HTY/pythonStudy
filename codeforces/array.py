n = int(input())
a = list(map(int, input().split()))

first_set = []
second_set = []
third_set = []
for i in range(len(a)):
    if a[i] < 0:
        first_set.append(a[i])
    if a[i] > 0:
        second_set.append(a[i])
    if a[i] == 0:
        third_set.append(a[i])

print("{} {}".format(len(first_set), first_set))
print("{} {}".format(len(second_set), second_set))
print("{} {}".format(len(third_set), third_set))