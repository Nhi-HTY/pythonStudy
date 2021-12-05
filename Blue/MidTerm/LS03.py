k, n, w = list(map(int, input().split()))
cost = 0
j = 1
for i in range(w):
    cost += (k*j)
    j += 1
borrow = cost - n
print(borrow) if borrow > 0 else print(0)