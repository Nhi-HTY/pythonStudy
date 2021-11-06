totalElement = list(map(int, input().split()))
elementInArray = list(map(int, input().split()))

firstArray = list(map(int, input().split()))
secondArray = list(map(int, input().split()))

leftOverFirstArray = firstArray[:elementInArray[0]]
leftOverSecondArray = []

i = 0
j = len(secondArray) - 1
while i < elementInArray[1]:
    leftOverSecondArray.append(secondArray[j])
    j -= 1
    i += 1

flag = True
if leftOverFirstArray[len(leftOverFirstArray) - 1] >= leftOverSecondArray[len(leftOverSecondArray) - 1]:
    flag = False

print("YES") if flag == True else print ("NO")
