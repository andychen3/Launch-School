"""

input: string
output: integer
rules:
1. only alphanumeric characters
2. disregarding case

DS - Dictionary

Algorithm:
1. Create a freq dict
2. Add up all the counts of each character case insenstiive to the dictionary
2a. initialize count = 0
3. Go through the values and add to count if the value is greater or equal to 2
4. return count


"""

def distinct_multiples(string):
    freq_dict = {}

    for char in string.lower():
        if char not in freq_dict:
            freq_dict[char] = 0
        freq_dict[char] += 1

    count = 0 

    for freq in freq_dict.values():
        if freq >= 2:
            count += 1
    return count    

print(distinct_multiples('xyz') == 0)               # (none)
print(distinct_multiples('xxyypzzr') == 3)          # x, y, z
print(distinct_multiples('xXyYpzZr') == 3)          # x, y, z
print(distinct_multiples('unununium') == 2)         # u, n
print(distinct_multiples('multiplicity') == 3)      # l, t, i
print(distinct_multiples('7657') == 1)              # 7
print(distinct_multiples('3141592653589793') == 4)  # 3, 1, 5, 9
print(distinct_multiples('2718281828459045') == 5)  # 2, 1, 8, 4, 5