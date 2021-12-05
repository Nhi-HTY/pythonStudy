n = int(input())
listScore = list(map(int, input().split()))

listStudent = []
for i in range(n):
    listStudent.append(listScore[i])

studentSort = []
listScore.sort(reverse=True)
for student in range(n):
    for score in range(n):
        if listStudent[student] == listScore[score]:
            studentSort.append(score + 1)
            break

for j in range(n):
    print(studentSort[j], end = " ")