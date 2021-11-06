a = int(input())

if a < 0:
    n = a * (-1)
else:
    n = a


def countn(n):
    if n < 10:
        return 1
    return 1 + countn(n//10)

print(countn(n))