t = int(input())

for _ in range(t):
    n = int(input())
    line = [0] + list(map(int, input().split()))
    l = 1
    r = line[-1] + 1
    ans = 0

    while l <= r:
        mid = (l+r) // 2
        k = mid
        isValid = True
        for i in range(1, n+1):
            if line[i] - line[i-1] > k:
                isValid = False
                break
            elif line[i] - line[i-1] == k:
                k -= 1

        if isValid:
            ans = mid
            r = mid - 1
        else:
            l = mid + 1

    print("Case {}: {}".format(_+1, ans))
