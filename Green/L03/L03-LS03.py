n = int(input())

min = n
max = n
while(1<2):
    n = int(input())
    if n == -1:
        break
    else:
        if min < n:
            if n > max:
                max = n
        else:
            min = n

print ("{} {}".format(max, min))


