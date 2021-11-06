import string

text = string.ascii_letters
textArray = []

for k in range(len(text)):
    textArray.append(text[k])

numbers = string.digits
numberArray = []

for l in range(len(numbers)):
    numberArray.append(numbers[l])

email = input()
localPart = ""
domainName = ""

special_characters = [".", "_"]

for i in range(len(email)):
    if email[i] == "@":
        for j in range(i, len(email) - 1):
            domainName += email[j + 1]
        break
    else:
        localPart += email[i]


def isValidLocalPart(local):
    if len(local) == 0:
        return False
    for m in range(len(local)):
        if (local[m] not in textArray) and (local[m] not in numberArray) and (local[m] not in special_characters):
            return False
    return True


def isValidDomainName(domain):
    count = 0
    if len(domain) == 0:
        return False
    for n in range(len(domain)):
        if domain[n] == ".":
            count += 1
        if (domain[n] not in textArray) and (domain[n] != "."):
            return False
        if (domain[n] == ".") and n != len(domain) - 1:
            if domain[n + 1] == ".":
                return False
    if count == 0:
        return False
    return True


if (isValidLocalPart(localPart) == True) and (isValidDomainName(domainName) == True):
    print("VALID")
else:
    print("INVALID")
