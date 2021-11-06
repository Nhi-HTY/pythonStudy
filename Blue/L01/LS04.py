inputString1 = input()
inputString2 = input()
ans1 = ""
isAns1 = True
ans2 =""
isAns2 = True

for i in range(len(inputString1)):
    if i == len(inputString1) - 1:
        if chr(ord(inputString1[i])) == "z":
            isAns1 = False
        if chr(ord(inputString2[i])) == "a":
            isAns2 = False
        ans1 += chr(ord(inputString1[i])+1)
        ans2 += chr(ord(inputString2[i]) - 1)
        break
    if ord(inputString1[i]) == ord(inputString2[i]) or (ord(inputString1[i]) == ord(inputString2[i]) - 1):
        ans1 += inputString1[i]
        ans2 += inputString2[i]
        continue
    if ord(inputString1[i]) < ord(inputString2[i]) - 1:
        if chr(ord(inputString1[i])) == "z":
            isAns1 == False
        if chr(ord(inputString2[i])) == "a":
            isAns2 == False
        ans1 += chr(ord(inputString1[i])+1) + inputString1[i+1:len(inputString1)]
        ans2 += chr(ord(inputString2[i]) - 1) + inputString2[i + 1:len(inputString2)]
        break
    else:
        ans2 += inputString2[i]


if ans1 != inputString1 and ans1 != inputString2 and ans2 != inputString1 and ans2 != inputString2:
    if isAns1:
        print(ans1)
    else:
        print(ans2)
else:
    print("No such string")