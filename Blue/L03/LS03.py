n = int(input())
listNum = list(map(int, input().split()))
start = end = 0

def isSorted(lst, key=lambda x: x):
    for i, el in enumerate(lst[1:]):
        if key(el) < key(lst[i]):
            return False
    return True
if n > 1:
    while start < n - 1:
        while end < n- 1:
            if listNum[end+1] > listNum[end]:
                break
            end += 1
        listNum[start:end+1] = sorted(listNum[start:end+1])
        if isSorted(listNum):
            print("yes")
            print(start+1, end = " ")
            print(end+1)
            exit()
        else:
            listNum[start:end + 1] = sorted(listNum[start:end + 1], reverse=True)
        start = end = end + 1

    print("no")
else:
    print("yes")
    print(start + 1, end=" ")
    print(end + 1)