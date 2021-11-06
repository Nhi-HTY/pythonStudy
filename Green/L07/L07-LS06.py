inputString = input()

unique_char =[]
unique_char.append(inputString[0])
isEqual = True

for i in range(len(inputString)):
    for j in range(len(unique_char)):
        if inputString[i] == unique_char[j]:
            isEqual = False
            break
        else:
            isEqual = True
    if isEqual == True:
        unique_char.append(inputString[i])
print(len(unique_char))
