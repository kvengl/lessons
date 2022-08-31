def UFO(n, data, octal):
    base = 8 if octal else 16
    return list(map(lambda x: convert_number(x, base), data))


def get_reversed_list_of_number(number):
    reversed_list = []
    count_digits = get_count_digits(number)
    for i in range(count_digits):
        reversed_list.append(number % 10 ** (i + 1) // (1 * (10 ** i)))
    return reversed_list


def get_count_digits(number):
    count = 0
    while number > 0:
        number //= 10
        count += 1
    return count


def convert_number(number, base):
    res = 0
    reversed_list = get_reversed_list_of_number(number)
    for i, digit in enumerate(reversed_list):
        res += digit * base ** i
    return res
