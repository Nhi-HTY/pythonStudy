n = int(input())

arrayInput = []
for m in range(0, n):
    a = list(map(int, input().split()))
    arrayInput.append(a)


arrayRowCount = len(arrayInput)
arrayColCount = len(arrayInput[0])
queenCount = 0

def is_queen(arrayInput, i, j, arrayRowCount, arrayColCount):
    tempMaxNumber = arrayInput[i][j]

    # Kiểm tra Row
    for z in range(arrayColCount):
        if arrayInput[i][z] > tempMaxNumber:
            return False

    # Kiểm tra cột
    for y in range(arrayRowCount):
        if arrayInput[y][j] > tempMaxNumber:
            return False

    # Kiểm tra đường chéo thứ 1
    crossRow = i + 1
    crossCol = j + 1
    while crossRow < i and crossCol + 1 < arrayColCount:
        if arrayInput[crossCol][crossRow] > tempMaxNumber:
            return False
        crossRow += 1
        crossCol += 1

    crossRow = i - 1
    crossCol = j - 1
    while crossRow >= 0 and crossCol - 1 >= 0:
        if arrayInput[crossCol][crossRow] > tempMaxNumber:
            return False
        crossRow -= 1
        crossCol -= 1

    # Kiểm tra đường chéo thứ 2
    crossRow = i + 1
    crossCol = j - 1
    while crossRow < i and crossCol - 1 >= 0:
        if arrayInput[crossCol][crossRow] > tempMaxNumber:
            return False
        crossRow += 1
        crossCol -= 1

    crossRow = i - 1
    crossCol = j + 1
    while crossRow >= 0 and crossCol < arrayColCount:
        if arrayInput[crossRow][crossCol] > tempMaxNumber:
            return False
        crossRow -= 1
        crossCol += 1
    return True


for i in range(arrayRowCount):
    for j in range(arrayColCount):
        if is_queen(arrayInput, i, j, arrayRowCount, arrayColCount):
            queenCount += 1

print(queenCount)