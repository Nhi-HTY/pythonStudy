a, b, c = map(float, raw_input().split())
peri = a + b + c
p = peri/2
s = (p*(p-a)*(p-b)*(p-c))**0.5

print ("{:.2f} {:.2f}".format(peri, s))