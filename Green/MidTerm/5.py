matrix = []
for i in range(0, 9):
    a = list(map(int, input().split()))
    matrix.append(a)

def checkRow(line):
    flag = True
    for row in range(0, line):
        j = 1
        while(j<=line):
            for x in matrix[row]:
                if x != j:
                    flag = False
                else:
                    flag = True
                    break
            j += 1
            if flag == False:
                return False
                break
    return True

def checkColumn(line):
    flag = True
    for column in range(0, line):
        j = 1
        while (j <= line):
            for row in range(0, line):
                if matrix[row][column] != j:
                    flag = False
                else:
                    flag = True
                    break
            j += 1

            if flag == False:
                return False
                break
    return True

def checkSubGrid(line):
    flag = True
    for start1 in range(0, line, 3):
        for start2 in range(0, line, 3):
            subItem = []
            for col in range(start2, start2 + 3):
                for row in range(start1, start1 +3):
                    subItem.append(matrix[row][col])
            j = 1
            while (j <= line):
                for x in subItem:
                    if x != j:
                        flag = False
                    else:
                        flag = True
                        break
                j += 1
            if flag == False:
                return False
                break
    return  True

def isSoduko():
    if checkRow(9) == True and checkColumn(9) == True and checkSubGrid(9) == True:
        return True
    return False

if isSoduko() == True:
    print("YES")
else:
    print("NO")
