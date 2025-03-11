'''
Q:
1. What is consecutive?

input: list of integers
output: an integer which is min sum of 5 consecutive nums. But if original list
is less than 5 elements return None
rules:
1. List can't be modified


running sum = min(sum)
left pointer  = 0

0 1 2 3 4 5
1 2 3 4 5 6

left = 1
right 5

5 - 1 + 1

 - 1 = 20


Algorithm:
1. Check len of list and if it is less than 5 return None
2. intiialize running sum = float("inf")
3. initialize left pointer to 0
4. Iterate through the numbers
5. have a while condiiton to close the window if there are more then 5 numbers
6. compare the running_sum to what is current and if it is less then save it
7. return running sum

'''

def minimum_sum(lst):
    if len(lst) < 5:
        return None
    
    min_sum = float("inf")
    left = 0
    curr_sum = 0

    for right, num in enumerate(lst):
        curr_sum += num

        while right - left + 1 >= 5: 
            min_sum = min(curr_sum, min_sum)
            curr_sum -= lst[left]
            left += 1

    return min_sum

print(minimum_sum([1, 2, 3, 4]) is None)
print(minimum_sum([1, 2, 3, 4, 5, -5]) == 9)
print(minimum_sum([1, 2, 3, 4, 5, 6]) == 15)
print(minimum_sum([55, 2, 6, 5, 1, 2, 9, 3, 5, 100]) == 16)
print(minimum_sum([-1, -5, -3, 0, -1, 2, -4]) == -10)