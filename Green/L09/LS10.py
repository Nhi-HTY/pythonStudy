import string
string.ascii_letters

n = int(input())

def findHexa(n):
    remainder = n % 16
    if remainder <= 9:
        result = chr(remainder + 48)
    else:
        result = chr(remainder + 55)
    if n<16:
        return result
    return findHexa(n // 16) + result

print(findHexa(n))