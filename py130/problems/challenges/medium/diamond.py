# https://launchschool.com/exercises/5ea8a7f4

"""
input: a letter
output: a diamond shape
rules:

A B C D E
0 1 2 3 4 

0, 2

1
 A 
B B
 A
 

0, 3
  A
 B B
C   C
 B B
  A
    A
   B B <-2
  C   C <- 4
 D     D <- 6
E       E <- 8
 D     D
  C   C
   B B
    A


 A
B B
 A
  A
 B B
C   C
 B B
  A


DS:
- Hashmap to create dictionary of values 


Algo:

"""
class Diamond:
    LETTER_MAP_CHAR = {letter: i for i, letter in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ")}
    LETTER_MAP_DIGITS = {i: letter for i, letter in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ")}

    @classmethod
    def make_diamond(cls, letter):

        letter_value = cls.LETTER_MAP_CHAR[letter]
        res = []

        for i in range(letter_value + 1):
            current_letter = cls.LETTER_MAP_DIGITS[i]
            spaces = " " * (letter_value - cls.LETTER_MAP_CHAR[current_letter])
            middle_spaces = " " * (i * 2 - 1)
            if i == 0:
                res.append(f"{spaces}{current_letter}{spaces}\n")
            else:
                res.append(f"{spaces}{current_letter}{middle_spaces}{current_letter}{spaces}\n")
                
        for i in range(letter_value - 1, -1, -1):
            current_letter = cls.LETTER_MAP_DIGITS[i]
            spaces = " " * (letter_value - cls.LETTER_MAP_CHAR[current_letter])
            middle_spaces = " " * (i * 2 - 1)
            if i == 0:
                res.append(f"{spaces}{current_letter}{spaces}\n")
            else:
                res.append(f"{spaces}{current_letter}{middle_spaces}{current_letter}{spaces}\n")
        
        return "".join(res)

# print(Diamond.make_diamond("C"))