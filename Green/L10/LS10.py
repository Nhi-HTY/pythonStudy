class Apple():
    def __init__(self, weight, price):
        self.w = weight
        self.p = price

    def findApple(self):
        max = 0
        for i in range(0, len(weight)):
            if self.w[max] < self.w[i] or(self.w[max] == self.w[i]
                                          and self.p[max] < self.p[i]):
                max = i
        return max

n = int(input())
weight = []
price = []

i = 0
while (i < n):
    x = list(map(int, input().split()))
    weight.append(x[0])
    price.append(x[1])
    i += 1

x = Apple(weight, price)
result = x.findApple()

print(result)



