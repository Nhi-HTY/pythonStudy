n = int(input())
flag = True

for i in range(2, n):
    if n % i == 0:
        flag = False
        break

if n == 1:
    print ("NO")
elif n == 0 or flag == True:
    print ("YES")
else:
    print ("NO")
