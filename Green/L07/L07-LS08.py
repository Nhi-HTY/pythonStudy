inputString = input()

ans = ""
eachWord = ""

flag = False

for i in range(len(inputString)):
    if inputString[i] != " ":
        eachWord += inputString[i]
    if inputString[i] == " ":
        eachWord = " " + eachWord
        flag = True
    if flag == True or i == len(inputString)-1:
        ans = eachWord + ans
        flag = False
        eachWord = ""
print(ans)