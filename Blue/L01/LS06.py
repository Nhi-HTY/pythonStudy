n = int(input())
matrix = []

i = 0

def isCover(a, b, c, d):
    if a <= c and d <= b:
        return True
    else:
        return False

while i < n:
    array = list(map(int, input().split()))
    matrix.append(array)
    i += 1

for j in range(n):
    isSegment = True
    for k in range(n):
        if j !=k :
            if not isCover(matrix[j][0], matrix[j][1], matrix[k][0], matrix[k][1]):
                isSegment = False
                break
    if isSegment:
        ans = j + 1
        break
    else:
        ans = -1

print(ans)
