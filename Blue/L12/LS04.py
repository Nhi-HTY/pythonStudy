def LowerBound(x, listGirl):
    pos = -1
    l = 0
    r = len(listGirl) - 1
    while l <= r:
        mid = int((l + r) / 2)
        if listGirl[mid] < x:
            pos = max(pos, mid)
            l = mid + 1
        else:
            r = mid - 1
    return pos

def UpperBound(x, listGirl):
    pos = girl
    l = 0
    r = len(listGirl) - 1
    while l <= r:
        mid = int((l + r) / 2)
        if listGirl[mid] > x:
            pos = min(pos, mid)
            r = mid - 1
        else:
            l = mid + 1
    return pos


girl = int(input())
listGirl = list(map(int, input().split()))
test = int(input())
listTest = list(map(int, input().split()))
for x in listTest:
    pos = LowerBound(x, listGirl)
    if pos == -1:
        ans = "X"
    else:
        ans = str(listGirl[pos])
    pos = UpperBound(x, listGirl)
    if pos == girl:
        ans += " X"
    else:
        ans += " " + str(listGirl[pos])

    print(ans)

