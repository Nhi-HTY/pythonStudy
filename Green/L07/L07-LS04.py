n = int(input())

for i in range(0, n):
    inputString = input()
    ans = inputString[0].upper()
    doUpperCase = False
    for j in range(1, len(inputString)):
        if doUpperCase == True:
            ans += inputString[j].upper()
            doUpperCase = False
        elif inputString[j] == " ":
            ans += inputString[j]
            doUpperCase = True
        else:
            ans += inputString[j].lower()
    print(ans)