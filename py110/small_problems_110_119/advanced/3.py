# https://launchschool.com/exercises/564614de?track=python


'''
input: matrix
output: new matrix rotated 90 degrees
rules:

row = 2
col = 4

0 1 2 3

3 7 4 2 | 0
5 1 0 8 | 1


row = 4
col = 2

5 3
1 7
0 4
8 2

[[5, 3]]


0 1 2

1 5 8 | 0
4 7 2 | 1
3 9 6 | 2


3 4 1
9 7 5
6 2 8 

for c in col -> 3
    sub_list = [1, 4, 3]
    for r in row -> 3
    c = 0
    r = 2
    sub_list.append(matrix[r][c]) # reverse


Algorithm:
1. Create empty matrix
2. iterate from colum
3. initialize empty sublist
4. itereate through row
5. append reversed(row and column. )
6. return list


'''

matrix1 = [
    [1, 5, 8],
    [4, 7, 2],
    [3, 9, 6],
]

matrix2 = [
    [3, 7, 4, 2],
    [5, 1, 0, 8],
]

def rotate90(matrix):
    row, col = len(matrix), len(matrix[0])
    new_matrix = []

    for c in range(col):
        sub_list = []
        for r in range(row):
            sub_list.append(matrix[r][c])
        new_matrix.append(sub_list[::-1])
    
    return new_matrix


new_matrix1 = rotate90(matrix1)
new_matrix2 = rotate90(matrix2)
new_matrix3 = rotate90(rotate90(rotate90(rotate90(matrix2))))

# These examples should all print True
print(new_matrix1 == [[3, 4, 1], [9, 7, 5], [6, 2, 8]])
print(new_matrix2 == [[5, 3], [1, 7], [0, 4], [8, 2]])
print(new_matrix3 == matrix2)