n, x = map(int, input().split())
listNum = list(map(int, input().split()))
def findNum(listNum, x):
    leftList = listNum[:n//2]
    rightList = listNum[n//2:len(listNum)]

    if x == leftList[len(leftList)-1]:
        print(len(leftList))
    elif x == rightList[0]:
        print(len(leftList)+1)
    elif x < leftList[len(leftList)-1]:
        flag = False
        for i in range(0, len(leftList)):
            if x == leftList[i]:
                print(i+1)
                flag = True
                break
        if flag == False:
            print(-1)
    elif x > rightList[0]:
        flag = False
        for j in range(0, len(rightList)):
            if x == rightList[j]:
                print(len(leftList)+j+1)
                flag = True
                break
        if flag == False:
            print(-1)

findNum(listNum, x)