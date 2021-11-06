def check_systemmaric(n):
    a = str(n)
    b = str(n)[::-1]
    return a==b

n = int(input())
if check_systemmaric(n) == True:
    print("YES")
else:
    print("NO")