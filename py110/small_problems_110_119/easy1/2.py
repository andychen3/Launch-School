# https://launchschool.com/exercises/407bf4aa

def is_palindrome(string):
    left = 0
    right = len(string) - 1

    while left < right:
        left_char = string[left]
        right_char = string[right]

        if left_char == right_char:
            left += 1
            right -= 1
        elif left_char != right_char:
            return False
        
    return True

# All of these examples should print True

print(is_palindrome('madam') == True)
print(is_palindrome('356653') == True)
print(is_palindrome('356635') == False)

# case matters
print(is_palindrome('Madam') == False)

# all characters matter
print(is_palindrome("madam i'm adam") == False)