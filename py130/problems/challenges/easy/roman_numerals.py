# https://launchschool.com/exercises/3d98b8dc

"""
input: number
output: string roman numeral
rules:
Every number before the 5 or 10s place you put the symbol in front.

III
IV - 4
V - 5
IX - 9
X - 10
XIV - 14
XV - 15
XIX - 19
XX
XXIV - 24


4
XIII
for 6

# If its 4 or 9 check + 1 if its in the dict

dict = {map to the roman numerals}

5


res = [X, V]
i = 1

while i < input:
    mod the i by 10: basing off of the remainder
    if the mod is 0. if i in dict:
        add it to res
        If i is greater or equal to what is in res you pop
    elif i reach 4 or 9:
        4 = IV, 9 = IX
        add + 1 then check for it in the dict
        Then use the dict to remove from res if the value of the roman numeral
        is less than the current
    else:
        I
    
    i += 1

return joined res


DS:
Dict - That holds the important values like I, V, X, L, C, D, M


Algo:   


"""
class RomanNumeral:
    
    def __init__(self, number):
        self.number = number
        self.roman_map = {5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M", "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


    def to_roman(self):
        num = 1
        res = []

        while num <= self.number:
            ones_place = num % 10
            if (ones_place == 0 or ones_place == 5) and num in self.roman_map:
                roman_numeral = self.roman_map.get(num, None)
                while roman_numeral and res and ones_place >= self.roman_map.get(res[-1], None):
                    res.pop()
                res.append(roman_numeral)
            elif ones_place == 4 or ones_place == 9:
                roman_numeral = self.roman_map[ones_place + 1]
                while roman_numeral and res and ones_place + 1 >= self.roman_map.get(res[-1], None):
                    res.pop()
                res.append("I")
                res.append(roman_numeral)
            else:
                res.append("I")
            num += 1
        return "".join(res)


