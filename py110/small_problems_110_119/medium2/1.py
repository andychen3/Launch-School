# https://launchschool.com/exercises/5800a75a?track=python

'''

input: string
output: dictionary - 
    1. % of chars in the string that are lowercaase
    2. % of chars that are upper
    3. % of chars that are neither


rules:
1. % are strings whose numeric values are between 0.00 and 100.00
2. Rounded to two decimal places
3. Assume at least one char.
4. spaces are counted as neither

Algorithm:
1. find length of string
2. create 3 buckets - lower, upper, and neither
3. Iterate through the string and depending on condiiton add to bucket
4. Create dictionary with the buckets as values and the keys of lower, upper, and neither
5. round to 2 decimal places


'''
def convert_to_percentage(number, length):
    return (number / length) * 100


def letter_percentages(string):
    length = len(string)
    lower = 0
    upper = 0
    neither = 0

    for char in string:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
        else:
            neither += 1
    

    return {"lowercase": f"{convert_to_percentage(lower, length):.2f}", 
            "uppercase": f"{convert_to_percentage(upper, length):.2f}",
             "neither": f"{convert_to_percentage(neither, length):.2f}"}

expected_result = {
    'lowercase': "50.00",
    'uppercase': "10.00",
    'neither': "40.00",
}
print(letter_percentages('abCdef 123') == expected_result)

expected_result = {
    'lowercase': "37.50",
    'uppercase': "37.50",
    'neither': "25.00",
}
print(letter_percentages('AbCd +Ef') == expected_result)

expected_result = {
    'lowercase': "0.00",
    'uppercase': "0.00",
    'neither': "100.00",
}
print(letter_percentages('123') == expected_result)