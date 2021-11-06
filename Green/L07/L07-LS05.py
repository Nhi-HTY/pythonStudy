n = int(input())

array = []
for m in range(0, n):
    a = input()
    array.append(a)

# sorting each letter in a word
for i in range(len(array)):
    word = array[i]
    array_char = []
    for j in range(len(word)):
        array_char.append(word[j].upper())
    array_char.sort()

    # find the min char in a word
    minChar = ""
    minLength = len(array_char)+1

    while len(array_char) > 0:
        tmpMinArray = []
        tmpMinArray.append(array_char[0])
        tmpMinChar = array_char[0]
        array_char.pop(0)
        for k in range(len(array_char)):
            if array_char[0] == tmpMinChar:
                tmpMinArray.append(array_char[0])
                array_char.pop(0)
            else:
                break
        if len(tmpMinArray) < minLength:
            minLength = len(tmpMinArray)
            minChar = tmpMinChar
    print(minChar)
