bookAndMinute = list(map(int, input().split()))
listTime = list(map(int, input().split()))

totalBook = bookAndMinute[0]
freeTime = bookAndMinute[1]
maxBook = 0
readTime = 0
start = 0

for end in range(totalBook):
    readTime += listTime[end]

    while readTime > freeTime:
        readTime -= listTime[start]
        start += 1

    maxBook = max(maxBook, end - start + 1)

print(maxBook)