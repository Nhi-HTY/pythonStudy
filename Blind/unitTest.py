import unittest
from MainProgram import ScrabbleScore


class TestSumScores(unittest.TestCase):
    # Setting up for the test
    def setUp(self):
        pass

    # Cleaning up after the test
    def tearDown(self):
        pass

    # Upper-case and lower-case letters should have the same value
    def test_uppercase_a(self):
        sumScore = ScrabbleScore()
        ans = sumScore.sumScore("A")
        self.assertEqual(ans, 1)

    def test_lowercase_a(self):
        sumScore = ScrabbleScore()
        ans = sumScore.sumScore("a")
        self.assertEqual(ans, 1)

    # The numbers are added up correctly for a given word
    def test_string_a(self):
        sumScore = ScrabbleScore()
        ans = sumScore.sumScore("b")
        self.assertEqual(ans, 3)

    # Prompts will be given asking the user to enter a valid word if the user does not enter a valid word.
    def test_invalid_word(self):
        sumScore = ScrabbleScore()
        ans = sumScore.sumScore("09883++_?")
        error = "You must enter valid word"
        self.assertEqual(ans, error)




if __name__ == '__main__':
    unittest.main()