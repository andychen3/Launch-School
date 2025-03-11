# https://launchschool.com/exercises/7c525401

'''
Questions:
1. Do i have to account for invalid input?
2. Will it always be numbers?
3. what happens if i get zero?
4. Non-negative?
5. Will count ever be bigger than the length of the number?


input: integer
output: integer
rules:
1. rotate starting from the left

count = 2
735291 -> 735219
0 1 2 3 4 5 

number_to_move = slice[-2]
left_side = slice[:-2]
right_side = slice[:count - 1]

left_side + right_side + number_to_move
convert back to integer

pseudocode:
1. Convert input num to string
2. Find location of number to move
3. Move the number to the end
4. combine number
5. convert back to integer
6. return number




'''
def rotate_rightmost_digits(num, count):
    if count == 1:
        return num
    
    string_num = str(num)
    end = string_num[-count]
    left_side = string_num[:-count]
    right_side = string_num[1 - count:]

    return int(left_side + right_side + end)

print(rotate_rightmost_digits(735291, 2) == 735219)  # True
print(rotate_rightmost_digits(735291, 3) == 735912)  # True
print(rotate_rightmost_digits(735291, 1) == 735291)  # True
print(rotate_rightmost_digits(735291, 4) == 732915)  # True
print(rotate_rightmost_digits(735291, 5) == 752913)  # True
print(rotate_rightmost_digits(735291, 6) == 352917)  # True
print(rotate_rightmost_digits(1200, 3) == 1002)      # True