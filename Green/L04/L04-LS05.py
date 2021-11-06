def find_max(n):
    length = len(str(n))
    tmpMax = 0
    for i in range(length):
        for j in range(i + 1, length):
            if n[i] < n[j]:
                tmpMax = n[j]
                break

    return tmpMax


print(find_max('34953'))
