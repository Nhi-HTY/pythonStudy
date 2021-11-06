# n = int(input())
# a = list(map(int, input().split()))

# smallest = 1
# i = 0
# unused = 1
# while(i<=100000):
#     for j in range(len(a)):
#         if a[j] == smallest:
#             smallest += 1
#             unused = smallest
#             break
#     i += 1
# print(unused)

# temp = [False]*100001
# ans = -1
# for i in a:
#     temp[i] = True
#
# for i in range (1, 100001):
#     if (temp[i] == False):
#         ans = i
#         break
# print(ans)
#

n = int(input())
a = list(map(int, input().split()))

smallest = 1
i = 0
unused = 1
while(i<len(a)):
    for j in range(len(a)):
        if a[j] == smallest:
            smallest += 1
            unused = smallest
            break
    i += 1
print(unused)