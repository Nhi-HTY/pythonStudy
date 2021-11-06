n = int(input())

current = n
flag = True
while (1<2):
    n = int(input())
    if (n == 0):
        break
    if current <= n:
        current = n
    else:
        flag = False

if flag == True:
    print ("YES")
else:
    print ("NO")
