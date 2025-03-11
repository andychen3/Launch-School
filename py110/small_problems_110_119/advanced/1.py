#https://launchschool.com/exercises/8a772030?track=python

'''
Questions:
1. Can the input be empty?
2. Do i have to account for invalid input or is it always going to be
a valid matrix.

input: nested list (matrix)
output: nested list (matrix)
rules:
1. don't modify original matrix

1 5 8
4 7 2
3 9 6 

1 5 8
0 1 2 <- index

new_matrix = 
1 4
5 7
8 2

for r in range(len(matrix))
    for c in range of matrix
    row = 1
    c = 2
    new_matrix[c][r] = original[r][c]

1 4 3
5 7 9
8 2 6




Algorithm:
1. Create empty matrix 3x3 filled with zeros
2. Itereate through rows
3. itereate through columns
4. access original matrix and access new matrix but switching the rows and columns
5. return new matrix

'''

matrix = [
    [1, 5, 8],
    [4, 7, 2],
    [3, 9, 6],
]

def transpose(matrix):
    row, col = len(matrix), len(matrix[0])
    new_matrix = [[None for _ in range(row)] for _ in range(col)]

    for r in range(row):
        for c in range(col):
            new_matrix[c][r] = matrix[r][c]

    return new_matrix

new_matrix = transpose(matrix)

print(new_matrix == [[1, 4, 3], [5, 7, 9], [8, 2, 6]]) # True
print(matrix == [[1, 5, 8], [4, 7, 2], [3, 9, 6]])     # True