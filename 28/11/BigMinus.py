def BigMinus(s1, s2):
    s1_len = len(s1)
    s2_len = len(s2)

    if s2_len > s1_len:
        s1 = add_zeros(s1, s2_len - s1_len)
    else:
        s2 = add_zeros(s2, s1_len - s2_len)

    minuend, deductible = get_minuend_deductible(list(s1), list(s2))

    res = []
    for i in range(len(minuend) - 1, -1, -1):
        n1 = int(minuend[i])
        n2 = int(deductible[i])

        if n1 - n2 < 0:
            minuend[i - 1] = str(int(minuend[i - 1]) - 1)
            res.append(str(n1 - n2 + 10))
        else:
            res.append(str(n1 - n2))

    normalized_res = ""
    is_ended_zeros_in_start = False
    for i in range(len(res) - 1, -1, -1):
        if res[i] == "0" and not is_ended_zeros_in_start:
            continue
        if res[i] != "0" or is_ended_zeros_in_start:
            is_ended_zeros_in_start = True
            normalized_res += res[i]
    if len(normalized_res) == 0:
        return "0"
    return normalized_res


def add_zeros(s, count):
    zeros = ""
    for i in range(count):
        zeros += "0"
    return zeros + s


def get_minuend_deductible(arr1, arr2):
    is_more_first = False
    for i in range(len(arr1)):
        n1 = int(arr1[i])
        n2 = int(arr2[i])
        if n1 > n2:
            is_more_first = True
            break
        elif n1 < n2:
            break
    if is_more_first:
        return arr1, arr2
    return arr2, arr1
