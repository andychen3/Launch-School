# https://launchschool.com/exercises/bc977f27

'''
Questions:


Input: string
Output: list of substrings
Explicit:
1. single chars are not palindromes
2. case sensitive.
3. duplicates are allowed. 
4. sorted by order of appearance in input string
Implicit:
1. punctuations are okay

Data structures
1. Use a list to hold the answer and to build up each individual substrings

Pseudocode:
1. check if palindrome
    1a. single chars are not considered palindromes
    2a. check case sensitivity

    compare original string to reversed string and if it is equal then
        return True
    else:
        return False

2. create the substrings
    0. result = []
    1. iterate starting at the first index. Then build substring starting from the
    second onwards.
    2. Move to next index then repeat. (nested loop)
    3. Iterate through substring list and pass in each substring to palindrome checker
    4. if palindrome append to result
    5. return result

madam
0 1 2 3 4 

madam
adam
dam
am
m

'''
def check_for_palindrome(string):
    if len(string) == 1:
        return False
    elif string == string[::-1]:
        return True
    else:
        return False

def palindromes(string):
    result = []
    list_of_substrings = [string[idx:i + 1] for idx in range(len(string) - 1) for i in range(idx, len(string))]
    print(list_of_substrings)
    for substring in list_of_substrings:
        if check_for_palindrome(substring):
            result.append(substring)
    
    return result


# print(palindromes('abcd') == [])                  # True
print(palindromes('madam') == ['madam', 'ada'])   # True 
# print(palindromes('hello-madam-did-madam-goodbye') ==
#                   [
#                       'll', '-madam-', '-madam-did-madam-',
#                       'madam', 'madam-did-madam', 'ada',
#                       'adam-did-mada', 'dam-did-mad',
#                       'am-did-ma', 'm-did-m', '-did-',
#                       'did', '-madam-', 'madam', 'ada', 'oo',
#                   ])    # True

# print(palindromes('knitting cassettes') ==
#                   [
#                       'nittin', 'itti', 'tt', 'ss',
#                       'settes', 'ette', 'tt',
#                   ])    # True