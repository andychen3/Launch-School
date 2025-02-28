# https://launchschool.com/exercises/4f333858

def is_real_palindrome(s):
    left, right = 0, len(s) - 1
    lowered_string = s.casefold()

    while left < right:
        left_char, right_char = lowered_string[left], lowered_string[right]

        if left_char.isalnum() and right_char.isalnum() and left_char == right_char:
            left += 1
            right -= 1
        elif not left_char.isalnum():
            left += 1
        elif not right_char.isalnum():
            right -= 1
        else:
            return False
        
    return True

print(is_real_palindrome('madam') == True)           # True
print(is_real_palindrome('356653') == True)          # True
print(is_real_palindrome('356635') == False)         # True
print(is_real_palindrome('356a653') == True)         # True
print(is_real_palindrome('123ab321') == False)       # True

# case doesn't matter
print(is_real_palindrome('Madam') == True)           # True

# only alphanumerics matter
print(is_real_palindrome("Madam, I'm Adam") == True) # True