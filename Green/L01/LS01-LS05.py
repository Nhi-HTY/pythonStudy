input = int(input())
sum = 0
for digit in str(input):
    sum += int(digit)

print (sum%10)

