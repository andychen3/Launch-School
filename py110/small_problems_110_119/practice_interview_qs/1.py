'''
Questions:
1. Invalid input?
2. What about empty list?


input: list of numbers
output: return resulting list
rules:
1. Only count unique values

set of original = {7}



Algorithm:
1. Create a set of the original values
2. Create an empty result
3. Iterate through the original list
4. Check the current number with each of the numbers in the set.
    4a. If the current number == to the number in the set skip
    4b. if it is less +1 to the count
    4c. return the count
5. append the count to the empty result


'''
def count_smaller_numbers(current_num, original_set):
    count = 0

    for num in original_set:
        if current_num > num:
            count += 1
    
    return count


def smaller_numbers_than_current(lst):
    nums_set = set(lst)
    result = []

    for num in lst:
        result.append(count_smaller_numbers(num, nums_set))
    
    return result

print(smaller_numbers_than_current([8, 1, 2, 2, 3]) == [3, 0, 1, 1, 2])
print(smaller_numbers_than_current([7, 7, 7, 7]) == [0, 0, 0, 0])
print(smaller_numbers_than_current([6, 5, 4, 8]) == [2, 1, 0, 3])
print(smaller_numbers_than_current([1]) == [0])

my_list = [1, 4, 6, 8, 13, 2, 4, 5, 4]
result   = [0, 2, 4, 5, 6, 1, 2, 3, 2]
print(smaller_numbers_than_current(my_list) == result)