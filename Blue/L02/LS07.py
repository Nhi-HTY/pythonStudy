n = int(input())
listChocolates = list(map(int, input().split()))

indexLeft = 0
indexRight = len(listChocolates)-1

totalLeft = listChocolates[indexLeft]
totalRight = listChocolates[indexRight]
i = 2

if len(listChocolates) == 1:
    left = 1
    right = 0
else:
    left = right = 1

while i < len(listChocolates):
    if totalLeft > totalRight:
        right += 1
        indexRight -= 1
        totalRight += listChocolates[indexRight]
        i += 1

    elif totalLeft < totalRight:
        left += 1
        indexLeft += 1
        totalLeft += listChocolates[indexLeft]
        i += 1

    else:
        if i == len(listChocolates) - 1:
            left += 1
            indexLeft += 1
            totalLeft += listChocolates[indexLeft]
            i += 1
        else:
            left += 1
            indexLeft += 1
            totalLeft += listChocolates[indexLeft]
            right += 1
            indexRight -= 1
            totalRight += listChocolates[indexRight]
            i += 2

print(left, end=" ")
print(right)
