def create_matrix(m,n):
    matrix = []
    for i in range(0,m):
        row = []
        for j in range(0,n):
            element = int(input(f"Element [{i}][{j}]: "))
            row.append(element)
        matrix.append(row)
    return matrix

def print_matrix_spiral(matrix):
    spiral_matrix = []
    top = 0
    bottom = len(matrix) - 1
    left = 0
    right = len(matrix[0]) - 1
    while top <= bottom and left <= right:
        for i in range(left,right+1):
            spiral_matrix.append(matrix[top][i])
        top += 1

        for i in range(top, bottom+1):
            spiral_matrix.append(matrix[i][right])
        right -= 1

        for i in range(right, left-1, -1):
            spiral_matrix.append(matrix[bottom][i])
        bottom -= 1

        for i in range(bottom, top -1, -1):
            spiral_matrix.append(matrix[i][left])
        left += 1
    print(spiral_matrix)

def print_matrix(A):
    max_len = max(len(str(i)) for row in A for i in row)
    for row in A:
        print("|" + ' '.join(f"{str(i):{max_len}}" for i in row) + "|")

m , n = map(int, input("Enter order m x n: ").split(" x "))
A = create_matrix(m,n)
print("Matrix A: ")
print_matrix(A)
print("Spiral format: ")
print_matrix_spiral(A)