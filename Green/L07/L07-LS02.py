inputString = input()

count = 0

for i in range(len(inputString)):
    if (ord(inputString[i]) >= ord("0") and ord(inputString[i]) <= ord("9")):
        count += 1

print(count)

