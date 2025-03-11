"""

input: string of digits
output: number of even numbered substring that can be formed
rules:
1. if a substring occurs more than once you count each occurence as a separate
substring


Algorithm:
0. initiate count to 0
1. iterate through string
2. nested loop starting from the idx + 1
2. convert the string to a number
3. mod by 2 to see if its even
4. if even add 1 to count
5. return count


"""


def even_substrings(string):
    count = 0

    for i in range(len(string)):
        for idx in range(i + 1, len(string) + 1):
            substring = string[i: idx]
            num = int(substring)
            if num % 2 == 0:
                count += 1
    return count

print(even_substrings('1432') == 6)
print(even_substrings('3145926') == 16)
print(even_substrings('2718281') == 16)
print(even_substrings('13579') == 0)
print(even_substrings('143232') == 12)