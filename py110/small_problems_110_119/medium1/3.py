# https://launchschool.com/exercises/89604c6e

'''
Questions:
1. 


input: integer
output: rotated integer
rules:

length = 6 
rotations = 6

while loop

735291 # 7
0 1 2 3 4 5

slice[:0] + slice[0 + 1:] + slice[0]

352917 # kept first digit
slice[:1] + slice[1 + 1:] + slice[1]

329175 # keep first 2
321759 # keep 3
321597 # keep 4
321579

pseudocode:
1. convert input to string
2. Keep count of how many rotations left
3. Rotate
4. decrement count of rotations
5. convert back to int
6. return


'''
def max_rotation(number):
    string_num = str(number)
    length = len(string_num)
    rotations = 0

    while rotations < length:
        end = string_num[rotations]
        left_side = string_num[:rotations]
        right_side = string_num[rotations + 1:]
        string_num = left_side + right_side + end
        rotations += 1
    
    return int(string_num)

print(max_rotation(735291) == 321579)          # True
print(max_rotation(3) == 3)                    # True
print(max_rotation(35) == 53)                  # True
print(max_rotation(8703529146) == 7321609845)  # True

# Note that the final sequence here is `015`. The leading
# zero gets dropped, though, since we're working with
# an integer.
print(max_rotation(105) == 15)                 # True

