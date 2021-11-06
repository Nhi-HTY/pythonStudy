n = int(input())
flag = True
for i in range (0, n):
    candies = int(input())
    if candies % 2 != 0:
        flag = False
if flag == True:
    print ("YES")
else:
    print ("NO")
