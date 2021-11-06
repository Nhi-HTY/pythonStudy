import string

validChar = string.ascii_letters


class Solution:
    def isPalindrome(self, s) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            i = left
            j = right
            while not s[i].isalnum() and i < j:
                i += 1
            while not s[j].isalnum() and j > 0:
                j -= 1

            if i < j and s[i].upper() != s[j].upper():
                return False
            left = i + 1
            right = j - 1
        return True


inputString = input()
solution = Solution()
print(solution.isPalindrome(inputString))

