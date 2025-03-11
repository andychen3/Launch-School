"""

input: nonempty string
output: tuple consisiting of a string and an integer (str, int)
rules:
1. lowercase alphabetic letters

s = argument
t = string component
k = integer

s == t * k



k = 0
t = 


Algorithm:
1. initialize k = 0
2. t = 0
3. iterate through string and find count of substring that i am building
4. as soon as the count is less than the max count ive found break
5. return tuple


"""

def repeated_substring(string):
    curr_substring = ""
    repeat = 0
    substring_answer = ""

    for char in string:
        curr_substring += char
        counts = string.count(curr_substring)
        if counts >= repeat:
            repeat = counts
            substring_answer = curr_substring
        else:
            break
    
    return (substring_answer, repeat)

print(repeated_substring('xyzxyzxyz') == ('xyz', 3))
print(repeated_substring('xyxy') == ('xy', 2))
print(repeated_substring('xyz') == ('xyz', 1))
print(repeated_substring('aaaaaaaa') == ('a', 8))
print(repeated_substring('superduper') == ('superduper', 1))