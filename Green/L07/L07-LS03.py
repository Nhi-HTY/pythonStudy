inputString = input()

ans = ""
length_ans = 0

flag = False

for i in range(len(inputString)):
    if inputString[i] == " ":
        if length_ans > 0:
            flag = True
    elif flag == True :
        ans += " "
        ans += inputString[i]
        length_ans += 2
        flag = False
    elif flag == False:
        ans += inputString[i]
        length_ans += 1

print(ans)

