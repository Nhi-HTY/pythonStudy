inputNum = []
for i in range(3):
    a = int(input())
    inputNum.append(a)
listAns = []

ans1 = inputNum[0] + inputNum[1] + inputNum[2]
listAns.append(ans1)

ans2 = inputNum[0] * inputNum[1] + inputNum[2]
listAns.append(ans2)

ans3 = inputNum[0] + inputNum[1] * inputNum[2]
listAns.append(ans3)

ans4 = (inputNum[0] + inputNum[1]) * inputNum[2]
listAns.append(ans4)

ans5 = inputNum[0] * (inputNum[1] + inputNum[2])
listAns.append(ans5)

ans6 = inputNum[0] * inputNum[1] * inputNum[2]
listAns.append(ans6)

max = listAns[0]
for x in listAns:
    if x > max:
        max = x
print(max)



