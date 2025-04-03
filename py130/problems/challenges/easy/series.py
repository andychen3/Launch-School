# https://launchschool.com/exercises/56f85e03

"""
input: string of digits
output: a list of the series that is passed to the method.
rules:
1. If the passed in argument is longer than the string length. throw error

[[0,1,2], [1,2,3], [2,3,4]]

01234

01
12

n = 2
i = 2

2:4

01, 12

012



DS:


Algo:


"""

class Series:

    def __init__(self, string_digit):
        self.string_digit = string_digit

    def slices(self, series_length):
        if series_length > len(self.string_digit):
            raise ValueError
        
        ans = []

        for i in range(len(self.string_digit)):
            temp = []
            for j in range(i, series_length + i):
                if j < len(self.string_digit):
                    temp.append(int(self.string_digit[j]))
            
            if len(temp) == series_length:
                ans.append(temp)

        return ans
