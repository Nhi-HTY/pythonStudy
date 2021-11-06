inputString = input()

lowerCase = inputString.lower()

flag = False

for i in range(len(inputString)):
    if (lowerCase[i] == "b" or lowerCase[i] == "i" or lowerCase[i] == "g" or lowerCase[i] == "o"):
        flag = True

if flag == False:
    print("NO")
else:
    print("YES")