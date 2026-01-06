def print_anti_diagonals(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    result = []
    

    
    for col in range(cols):
        i, j = 0, col
        diagonal = []
        while i < rows and j >= 0:
            diagonal.append(matrix[i][j])
            i += 1
            j -= 1
        result.append(diagonal)
        
        
    for row in range(1, rows):
        i, j = row, cols - 1
        diagonal = []
        while i < rows and j >= 0:
            diagonal.append(matrix[i][j])
            i += 1
            j -= 1
        result.append(diagonal)
        
    for diagonal in result:
        print(' '.join(map(str, diagonal)))
        
        
m, n = map(int, input().split())


matrix = []
for _ in range(m):
    row = list(map(int, input().split()))
    if len(row) != n:
        print(f"Error: each row must have exactly {n} numbers")
        exit(1)
    matrix.append(row)
    
    

    

print_anti_diagonals(matrix)
