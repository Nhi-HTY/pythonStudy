from nltk.corpus import words

class ScrabbleScore():
    def __init__(self):
        self.scores = {"a": 1, "e": 1, "i": 1, "o": 1, "u": 1, "l": 1,
                       "n": 1, "r": 1, "s": 1, "t": 1, "d": 2, "g": 2,
                       "b": 3, "c": 3, "m": 3, "p": 3, "f": 4, "h": 4,
                       "v": 4, "w": 4, "y": 4, "k": 5, "j": 8, "x": 8,
                       "q": 10, "z": 10}

    def sumScore(self, word):
        point = 0
        if word not in words.words():
            return self.promptError()
        for letter in word:
            point += self.scores[letter.lower()]
        return point

    def promptError(self):
        return "You must enter valid word"

if __name__ == '__main__':
    inputString = input()
    sumScore = ScrabbleScore()
    ans = sumScore.sumScore(inputString)
    print(ans)
