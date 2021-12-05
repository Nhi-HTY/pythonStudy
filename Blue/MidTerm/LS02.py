n = int(input())
word = input()
dictChar = {}

if n < 26:
    print("NO")
else:
    for i in range(n):
        if word[i].upper() not in dictChar:
            dictChar[word[i].upper()] = "1"
        else:
            n -= 1
    print("YES") if n >= 26 else print("NO")