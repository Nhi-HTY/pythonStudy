def isPalindrome(x) -> bool:
    if x < 0:
        return False
    else:
        x = str(x)
        left = 0
        right = len(x)-1
        return checkPalindrom(left, right, x)

def checkPalindrom(left, right, x):
    if left == right:
        return True
    if left == right - 1 and x[left] == x[right]:
        return True
    if x[left] == x[right]:
        return checkPalindrom(left + 1, right - 1, x)
    return False

if __name__ == "__main__":
    x = int(input())
    isPalindrome(x)