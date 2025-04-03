# https://launchschool.com/exercises/b5038c34

"""
input: string, list of strings
output: list of strings that are anagram of string
rules:
1. case sensitive. So if upper or lower case does not match it. 

DS:


Algo:


"""

class Anagram:

    def __init__(self, string):
        self.string = string.lower()

    def match(self, list_of_strings):
        """
        List of strings are potential anagrams
        """
        res = []

        key = "".join(sorted(self.string))


        for string in list_of_strings:
            if string.lower() == self.string:
                continue
            
            sorted_string = "".join(sorted(string.lower()))
            
            if sorted_string == key:
                res.append(string)
        
        return res
