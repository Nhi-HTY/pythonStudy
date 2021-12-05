n, k = map(int, input().split())
listNum = list(map(int, input().split()))
fre = [0] * (10 ** 5 + 5)
unique = 0
j = 0

for i in range(n):
    if fre[listNum[i]] == 0:
        unique += 1

    fre[listNum[i]] += 1

    while unique == k:
        fre[listNum[j]] -= 1

        if fre[listNum[j]] == 0:
            print(j + 1, i + 1)
            exit()

        j += 1

print('-1 -1')