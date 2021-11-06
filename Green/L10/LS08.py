class Fraction:
    def __init__(self, x, y):
        self.nu = x
        self.de = y
    def compare(self, other):
        return self.nu * other.de - self.de * other.nu
    def GCD(self):
        a = self.nu
        b = self.de
        while (b != 0):
            r = a % b
            a = b
            b = r
        return a
    def reduce(self):
        gcd = self.GCD()
        self.nu //= gcd
        self.de //= gcd

n = int(input())

lst = []

for i in range(n):
    x, y = map(int, input().split(' '))
    lst.append(Fraction(x, y))

ans = lst[0]
for x in lst:
    for j in range(0, n):
        if (ans.compare(lst[j]) <= 0):
            ans = lst[j]

ans.reduce()
print(ans.nu, ans.de)