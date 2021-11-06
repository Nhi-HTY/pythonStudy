string = input()

ans = ""
ans = string[0].upper()

for i in range(len(string)):
    if string[i] == " ":
        firstLetter = string[i+1].upper()
        ans += firstLetter

print(ans)