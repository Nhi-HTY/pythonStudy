password = list(map(int, input().split()))
i = 0
listPass = []
while i < password[0] + 1:
    singlePass = input()
    listPass.append(singlePass)
    i += 1

bestCase = 1
worstCase = 0
correctPass = listPass[len(listPass) - 1]
totalPswNeedToEnterInWorstCase = 0
totalPswNeedToEnterInBestCase = 0

for j in range(len(listPass) - 1):
    if len(listPass[j]) < len(correctPass):
        totalPswNeedToEnterInBestCase += 1
    if len(listPass[j]) <= len(correctPass):
        totalPswNeedToEnterInWorstCase += 1

bestCase += totalPswNeedToEnterInBestCase//password[1] * 5 + totalPswNeedToEnterInBestCase

if password[1] < totalPswNeedToEnterInWorstCase:
    worstCase += (totalPswNeedToEnterInWorstCase-1)//password[1] * 5 + totalPswNeedToEnterInWorstCase
else:
    worstCase += totalPswNeedToEnterInWorstCase

print(bestCase, end=" ")
print(worstCase)