"""
input: two string arguments
output: return a number (the number is the times the second string occurs in the first)
rules:
1. overallping strings don't count
2. second argument is never empty
3. but first can be. and in that case return 0

Algorithm:

"""
def count_substrings(string, substring):
    return string.count(substring)

print(count_substrings('babab', 'bab') == 1)
print(count_substrings('babab', 'ba') == 2)
print(count_substrings('babab', 'b') == 3)
print(count_substrings('babab', 'x') == 0)
print(count_substrings('babab', 'x') == 0)
print(count_substrings('', 'x') == 0)
print(count_substrings('bbbaabbbbaab', 'baab') == 2)
print(count_substrings('bbbaabbbbaab', 'bbaab') == 2)
print(count_substrings('bbbaabbbbaabb', 'bbbaabb') == 1)