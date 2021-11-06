inputString = input()
minStep = 0

totalChar = ord("z") - ord("a") + 1
for i in range(len(inputString)):
    if i == 0:
        clockwise = ord(inputString[i]) - ord("a")
    else:
        clockwise = ord(inputString[i]) - ord(inputString[i-1])
    if clockwise < 0:
        clockwise *= -1
    counterClockwise = totalChar - clockwise
    if clockwise > counterClockwise:
        minStep += counterClockwise
    else:
        minStep += clockwise

print(minStep)