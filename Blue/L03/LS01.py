totalSubjects, time = map(int, input().split())
listSubject = list(map(int, input().split()))
totalTime = 0

listSubject.sort()
for i in range(totalSubjects):
    if time < 1:
        totalTime += listSubject[i]
    else:
        totalTime += time * listSubject[i]
        time -= 1

print(totalTime)