'''

input: list of integers
output: tuple of two numbers that are closet together in value
rules:
1. If there are multiple pairs that are equally close return the pair that occurs
first

12 22 7 17

pair = (12, 22)
min_dist = float("inf)
12 22

if less than:
    update pair

Algorithm:
1. initialize pair to empty tuple
2. min_dist to float(inf)
3. iterate throuigh the list from 0 to range of list
4. nested loop starting from idx 1 to end of list
5. find min _ dist if it is less than current min dist
6. update value of pair and min dist


'''

def closest_numbers(lst):
    pairs = ()
    min_dist = float("inf")

    for i, num in enumerate(lst):
        for idx in range(i + 1, len(lst)):
            abs_dist = abs(num - lst[idx])
            if abs_dist < min_dist:
                min_dist = abs_dist
                pairs = (num, lst[idx])

    return pairs

print(closest_numbers([5, 25, 15, 11, 20]) == (15, 11))
print(closest_numbers([19, 25, 32, 4, 27, 16]) == (25, 27))
print(closest_numbers([12, 22, 7, 17]) == (12, 7))



