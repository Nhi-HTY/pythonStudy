import sys
sys.setrecursionlimit(10000000)

n = int(input())
inputString = input()

inputArray =[]
reverse = []

for x in inputString:
    inputArray.append(x)

def reverseString(inputArray):
    last = inputArray[len(inputArray)-1]
    inputArray.pop(len(inputArray)-1)
    if len(inputArray) == 0:
        reverse.append(last)
    else:
        reverse.append(last)
        reverseString(inputArray)

reverseString(inputArray)
flag = True
for i in range(len(reverse)):
    if inputString[i] != reverse[i]:
        flag = False

if flag == True:
    print("YES")
else:
    print("NO")