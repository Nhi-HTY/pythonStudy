a, b = map(int, raw_input().split())
x = int(input())

if (x % a == 0 and x % b ==0):
    print("Both")
elif (x % a == 0):
    print ("Upan")
elif (x % b == 0):
    print ("Ipan")
else:
    print ("No")