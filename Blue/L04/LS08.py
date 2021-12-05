def findLongestLength(tag):
    listOpen = []
    ans = 0
    for i in range(len(tag)):
        if tag[i] == "<":
            listOpen.append(tag[i])
        else:
            if len(listOpen) == 0:
                break
            else:
                listOpen.pop()
                ans = i + 1 if len(listOpen) == 0 else ans
    return ans

n = int(input())
listTag = []
i = 0
while i < n:
    tag = input()
    listTag.append(tag)
    i += 1

for tag in listTag:
    print(findLongestLength(tag))
