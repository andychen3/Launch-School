# https://launchschool.com/exercises/d6014ce2

"""
input: string
output: the hamming distance which is a int
rules:
1. Hamming distance is only defined for sequences of equal length
2. If not equal compute the distance over the shorter length
3. Empty string is 0

DS:

1

GGACGG
GGTCG


Algo:
1. if either is empty string return 0
2. find length of both strings
3. Then while loop that the end of either string is not reached
4. compare each one to see if the same
5. count 1 to total if it is different
6 return


"""


class DNA:
    def __init__(self, sequence):
        self.sequence = sequence

    def hamming_distance(self, sequence):
        differences = 0

        for char1, char2 in zip(self.sequence, sequence):
            if char1 != char2:
                differences += 1

        return differences


