import math

a, b = map(int, input().split())

c = a//(math.gcd(a, b))
d = b//(math.gcd(a, b))


print("{} {}".format(c, d))