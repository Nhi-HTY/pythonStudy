# n = int(input())
# a = list(map(int, input().split()))
#
# flag = False
# for i in range(len(a)):
#     if a[i] == 0:
#         if (i+1 < len(a) and i+2 < len(a)):
#             if a[i+1] == 0 and a[i+2] == 0:
#                 if i + 3 < len(a):
#                     if a[i+3] == 0:
#                         flag = False
#                         break
#                     else:
#                         flag = True
#                 else:
#                     flag = False
#                     break
#         if (i + 1 > len(a)-1):
#             flag = False
#             break
#     else:
#         flag = True
#
# if flag == False:
#     print("NO")
# else:
#     print("YES")

n = int(input())
a = list(map(int, input().split()))
isGood = True
if a[-1] == 0:
    print ("NO")
else:
    for i in range(len(a)-3):
        if a[i] == 0 and a[i+1] ==0 and a[i+2] ==0 and a[i+3] == 0:
            isGood = False
            break
    if isGood == True:
        print ("YES")
    else:
        print("NO")

