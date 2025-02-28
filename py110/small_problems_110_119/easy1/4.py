# https://launchschool.com/exercises/8e9d667a

def running_total(nums):
    # input list of numbers
    out_put_list = []

    for num in nums:
        if not out_put_list:
            out_put_list.append(num)
        else:
            out_put_list.append(out_put_list[-1] + num)
    return out_put_list
    
    
    # output is a list of numbers with running total
print(running_total([2, 5, 13]) == [2, 7, 20])    # True
print(running_total([14, 11, 7, 15, 20])
      == [14, 25, 32, 47, 67])                    # True
print(running_total([3]) == [3])                  # True
print(running_total([]) == [])                    # True