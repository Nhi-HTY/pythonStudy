inputString = input()

listDup = []
flag = True
for i in range(0, len(inputString) - 1):
    j = i + 1
    while(j < len(inputString)):
        dupLetter = []
        if inputString[i] == inputString[j]:
            for row in range(0, len(listDup)):
                if listDup[row][0] == inputString[i]:
                    flag = False
            if flag == True:
                dupLetter.append(inputString[i])
                dupLetter.append(j)
                listDup.append(dupLetter)
        j += 1
        flag = True

if len(listDup) == 0:
    print("null")
else:
    ans = listDup[0][0]
    min = listDup[0][1]
    for row in range(1, len(listDup)):
        if listDup[row][1] < min:
            min = listDup[row][1]
            ans = listDup[row][0]
    print(ans)


