def TheRabbitsFoot(s, flag):
    if flag:
        return encode(s)
    return decode(s)


def encode(s):
    new_s = get_str_without_spaces(s)
    N = len(new_s)
    [row_len, col_len] = calc_matrix_size(N)
    matrix = fill_matrix_for_encode(new_s, row_len, col_len)
    cipher = get_cipher_by_matrix(matrix)
    return cipher


def decode(s):
    new_s = get_str_without_spaces(s)
    N = len(new_s)
    [row_len, col_len] = calc_matrix_size(N)

    list_without_spaces = s.split()
    for i in range(len(list_without_spaces)):
        while len(list_without_spaces[i]) < col_len:
            list_without_spaces[i] += " "
    new_s = "".join(list_without_spaces)

    matrix = fill_matrix_for_decode(new_s, row_len, col_len)
    original = get_original_by_matrix(matrix)
    return original


def get_str_without_spaces(s):
    new_s = ""
    for letter in s:
        if letter != " ":
            new_s += letter
    return new_s


def calc_matrix_size(N):
    size = N ** 0.5
    row_len = round(size)
    col_len = ceil(size)
    while row_len * col_len < N:
        row_len + 1
    return [row_len, col_len]


def get_cipher_by_matrix(matrix):
    cipher = ""
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            cipher += matrix[j][i]
            if j == len(matrix[i]) - 1 and i != len(matrix) - 1:
                cipher += " "
    return cipher


def get_original_by_matrix(matrix):
    original = ""
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            original += matrix[i][j]
    return original


def fill_matrix_for_encode(s, row_len, col_len):
    matrix = []
    s_ind = 0
    for i in range(row_len):
        matrix.append([])
        for j in range(col_len):
            if s_ind < len(s):
                matrix[i].append(s[s_ind])
                s_ind += 1
            else:
                matrix[i].append("")
    return matrix


def fill_matrix_for_decode(s, row_len, col_len):
    matrix = []
    s_ind = 0
    while len(matrix) < row_len:
        matrix.append([])
    for j in range(col_len):
        for i in range(row_len):
            if s_ind < len(s):
                matrix[i].append(s[s_ind])
                s_ind += 1
            else:
                matrix[i].append("")
    return matrix


def ceil(n):
    return int(-1 * n // 1 * -1)


def floor(n):
    return int(n // 1)
