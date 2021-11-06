class Solution:
    def __init__(self):
        self.roman = {"I" : 1, "V": 5, "X": 10,
                    "L" : 50, "C": 100, "D": 500,
                     "D": 500, "M": 1000}
        self.sum = 0
    def romanToInt(self, s: str) -> int:
        i = 0
        while i < len(s):
            if i+1 < len(s):
                if s[i] == "I":
                    if s[i+1] == "V":
                        self.sum += 4
                        i +=2
                    elif s[i+1] == "X":
                        self.sum += 9
                        i +=2
                    else:
                        self.sum += self.notSpecialCase(s[i])
                        i +=1
                elif s[i] == "X":
                    if s[i+1] == "L":
                        self.sum += 40
                        i +=2
                    elif s[i+1] == "C":
                        self.sum += 90
                        i +=2
                    else:
                        self.sum += self.notSpecialCase(s[i])
                        i +=1
                elif s[i] == "C":
                    if s[i+1] == "D":
                        self.sum += 400
                        i +=2
                    elif s[i+1] == "M":
                        self.sum += 900
                        i += 2
                    else:
                        self.sum += self.notSpecialCase(s[i])
                        i +=1
                elif s[i] in self.roman:
                    self.sum += self.roman[s[i]]
                    i += 1
            elif s[i] in self.roman:
                self.sum += self.roman[s[i]]
                i += 1
        return self.sum

    def notSpecialCase(self, s):
        return self.roman[s]

n = input()
a = Solution()
print(a.romanToInt(n))