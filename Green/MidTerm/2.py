n = int(input())

for i in range(n):
    space = " "*((n-i)-1)
    print(space, end="")
    for j in range(2*i+1):
            print("*", end="")
    print()