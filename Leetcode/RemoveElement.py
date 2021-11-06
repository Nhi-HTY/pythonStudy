def removeElement(inputArray, val) -> int:
    n = len(inputArray)
    k = 0

    for i in range(n):
        if inputArray[i] == val:
            inputArray[i] = -1

        else:
            k += 1

    start, end = 0, n - 1
    while start < end:
        if inputArray[start] != -1:
            start += 1
        else:
            while inputArray[end] == -1 and end >= 1 and start < end:
                end -= 1
            # now nums[end] > -1
            inputArray[start], inputArray[end] = inputArray[end], inputArray[start]
            start += 1
            end -= 1
    return k

inputArray = list(map(int, input().split()))
removeElement(inputArray, 3)
