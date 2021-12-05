antomDict = {"H": 1, "C": 12, "O": 16}
antom = input().strip()

listAntom = []
for i in range(len(antom)):
    if antom[i].isalpha():
        listAntom.append(antomDict[antom[i]])
    elif antom[i].isnumeric():
        listAntom.append(listAntom.pop()*int(antom[i]))
    elif antom[i] == "(":
        listAntom.append(-1)
    elif antom[i] == ")":
        total = 0
        while listAntom[-1] != -1:
            total += listAntom[-1]
            listAntom.pop()
        listAntom.pop()
        listAntom.append(total)

print(sum(listAntom))




