# https://launchschool.com/exercises/c7ca8683

"""
input: word
output: Computes scrabble score for that word (int)
rules:
1. List of letters with their values
2. Empty string is 0
3. whitespaces are 0. So use strip
4. None is 0
5. case insensitive - casefold()


DS:

alacrity - 1 + 1 + 1 + 3 + 1 + 1 + 1 + 4
Algo:

"""

class Scrabble:
    SCORE_1 = set("aeioulnrst")
    SCORE_2 = set("dg")
    SCORE_3 = set("bcmp")
    SCORE_4 = set("fhvwy")
    SCORE_5 = set("k")
    SCORE_8 = set("jx")
    SCORE_10 = set("qz")

    def __init__(self, word):
        self.word = word.casefold().strip() if word else None

    def score(self):
        """
        returns a score
        """
        if not self.word:
            return 0
        
        total = 0

        for char in self.word:
            if char in self.SCORE_1:
                total += 1
            elif char in self.SCORE_2:
                total += 2
            elif char in self.SCORE_3:
                total += 3
            elif char in self.SCORE_4:
                total += 4
            elif char in self.SCORE_5:
                total += 5
            elif char in self.SCORE_8:
                total += 8
            elif char in self.SCORE_10:
                total += 10
        return total
                
    @classmethod
    def calculate_score(cls, word):
        """
        can probably invoke score by creating a new word 
        and calling score and returning
        """
        new_word = Scrabble(word)
        return new_word.score()