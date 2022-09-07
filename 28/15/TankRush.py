def TankRush(row_count, col_count, s1, row2_count, col2_count, s2):
    if row2_count == 0 or col2_count == 0:
        return True
    if row2_count > row_count or col2_count > col_count:
        return False
    source_map, tanks_map = get_matrix_from_str(s1), get_matrix_from_str(s2)

    for i in range(row_count - row2_count + 1):
        for j in range(col_count - col2_count + 1):
            if source_map[i][j] != tanks_map[0][0]:
                continue
            if is_equal_matrices(get_submatrix(source_map, i, i + row2_count, j, j + col2_count), tanks_map):
                return True
    return False


def is_equal_matrices(source_map, tanks_map):
    for i in range(len(source_map)):
        for j in range(len(source_map[i])):
            if source_map[i][j] != tanks_map[i][j]:
                return False;
    return True


def get_submatrix(matrix, from_i, to_i, from_j, to_j):
    submatrix = []
    new_matrix = matrix[from_i:to_i]
    for rows in new_matrix:
        submatrix.append(rows[from_j:to_j])
    return submatrix;


def get_matrix_from_str(str):
    matrix = []
    rows = str.split()
    for row in rows:
        letters = list(row)
        matrix.append(letters)
    return matrix
