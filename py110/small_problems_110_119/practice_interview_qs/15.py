"""

input: string that is all numeric digits
output: return integer that is greatest product of four consecutive digits
rules:
1. Always have more than 4 arguments

product = 1
max_product = 0

23456
01234

left = 0
right = 3

3 - 0 + 1 = 4




Algorithm:
1. have product = 1 and max_product = 0
2. left = 0
3. iterate through string
4. convert string to num and then multiply to product
5. while loop to check if the length which is just right - left + 1 == 4
6. get max product
7. increase left + 1
8. return max_product

"""

def greatest_product(digits):
    product = 1
    max_product = 0
    left = 0

    for right, str_digit in enumerate(digits):
        num = int(str_digit)
        product *= num

        while right - left + 1 == 4:
            max_product = max(max_product, product)
            product /= int(digits[left])
            left += 1
    
    return max_product

print(greatest_product('23456') == 360)      # 3 * 4 * 5 * 6
print(greatest_product('3145926') == 540)    # 5 * 9 * 2 * 6
print(greatest_product('1828172') == 128)    # 1 * 8 * 2 * 8
print(greatest_product('123987654') == 3024) # 9 * 8 * 7 * 6