inputString = input()

s1 = ""
for i in range(len(inputString)):
    if i % 2 == 0:
        s1 += inputString[i]

s2 = ""
for i in range(len(inputString)):
    if i % 2 != 0:
        s2 += inputString[i]

reverseS2 = s2[::-1]
ans = ""
k = 0
m = 0
for j in range(len(inputString)):
    if j % 2 == 0:
        ans += s1[k]
        k+=1
    if j % 2 != 0:
        ans += reverseS2[m]
        m+=1
print(ans)
