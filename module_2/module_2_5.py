def get_matrix(n, m, value):
    matrix = []
    for i in range(0,n):
        matrix.append([])
        for j in range(0,m):
            matrix[i].append(value)
    return matrix
result1 = get_matrix(6,2,7)
result2 = get_matrix(3,4,6)
result3 = get_matrix(2,3,40)
print(result1, result2, result3, sep='\n')