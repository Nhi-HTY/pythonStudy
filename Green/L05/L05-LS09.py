# n = int(input())
# i = 0
# apple =[]
# orange =[]
# while(i<n):
#     x = list(map(int, input().split()))
#     apple.append(x[0])
#     orange.append(x[1])
#     i += 1
#
# total_max = 0
# orange_after =[]
#
# def find_max(a):
#     max = 0
#     for i in range(len(a)):
#         if a[i] > max:
#             max = a[i]
#     return max
#
#
# max_apple = find_max(apple)
# index =[]
#
# for i in range(len(apple)):
#     if apple[i] == max_apple:
#         index.append(i+1)
#         orange_after.append(orange[i])
#         total_max +=1
#
# if total_max > 1:
#     max_orange = find_max(orange_after)
#     for j in range(len(orange_after)):
#         if orange_after[j] == max_orange:
#             print(index[j])
#             break
# else:
#     print(index[0])

n = int(input())
i = 0
apple =[]
orange =[]
while(i<n):
    x = list(map(int, input().split()))
    apple.append(x[0])
    orange.append(x[1])
    i += 1

max_index = 0
for i in range(1, n):
    if apple[max_index]< apple[i] or (apple[max_index] == apple[i] and orange[max_index] < orange[i]):
        max_index = i
print(max_index+1)
