n = int(input())


if n <= 1:
    ans = n * 15000
elif n <= 5:
    ans = 15000 + (n-1) * 13500
elif n <12:
    ans = 15000 + 4 * 13500 + (n-5)*11000
else:
    ans = (15000 + 4 * 13500 + (n - 5) * 11000)*0.9

print(int(ans))