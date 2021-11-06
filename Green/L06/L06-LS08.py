# n = int(input())
#
# matrix = []
# for m in range(0, n):
#     a = list(map(int, input().split()))
#     matrix.append(a)
#
# def find_max_diagonal2(array, i, k, size):
#     array_diagonal2 = []
#     array_diagonal2.append(array[i][k])
#     m = i-1
#     n = k+1
#     while(n<size and n>=0 and m <size and m>=0):
#         array_diagonal2.append(array[m][n])
#         m -= 1
#         n +=1
#     g = i+1
#     h = k-1
#     while (g<size and g>=0 and h <size and h>=0):
#         array_diagonal2.append(array[g][h])
#         g +=1
#         h -=1
#     max =0
#     length = len(array_diagonal2)
#     for l in range(0, length):
#         if array_diagonal2[l] > max:
#             max = array_diagonal2[l]
#     return max
#
# def find_max_diagonal1(array, i, k, size):
#     array_diagonal1 = []
#     array_diagonal1.append(array[i][k])
#     m = i-1
#     n = k-1
#     while(n<size and n>=0 and m <size and m>=0):
#         array_diagonal1.append(array[m][n])
#         m -= 1
#         n -=1
#     g = i+1
#     h = k+1
#     while (g<size and g>=0 and h <size and h>=0):
#         array_diagonal1.append(array[g][h])
#         g +=1
#         h +=1
#     max =0
#     length = len(array_diagonal1)
#     for l in range(0, length):
#         if array_diagonal1[l] > max:
#             max = array_diagonal1[l]
#     return max
#
# total = 0
# indies = []
# for i in range(0, n):
#     max = 0
#     for j in range(0, n):
#         if matrix[i][j] > max:
#             max = matrix[i][j]
#     for k in range(0, n):
#         if matrix[i][k] == max:
#             max2 = 0
#             index = i
#             for l in range(0, n):
#                 if matrix[l][k] > max2:
#                     max2 = matrix[l][k]
#             for h in range (0, n):
#                 if matrix[h][k] == max2:
#                     indies.append(h)
#             for x in indies:
#                 if x == index:
#                     max_1 = find_max_diagonal1(matrix, i, k, n)
#                     if (matrix[i][k] == max_1):
#                         max_2 = find_max_diagonal2(matrix, i, k, n)
#                         if (matrix[i][k] == max_2):
#                             total += 1
#             indies = []
#
# print(total)
#
