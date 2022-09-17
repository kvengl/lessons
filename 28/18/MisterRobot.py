def MisterRobot(N, data):
    start_index = 2
    for i in range(start_index, N):
        code = data[i - 2], data[i - 1], data[i]
        if is_sorted_by_asc(code):
            continue
        result_can_ordered_by_asc = can_ordered_by_asc(code)
        is_can = result_can_ordered_by_asc['is_can']
        arr = result_can_ordered_by_asc['arr']
        if not is_can:
            return False
        data[i - 2] = arr[0]
        data[i - 1] = arr[1]
        data[i] = arr[2]
    return True


def can_ordered_by_asc(arr):
    is_can = False
    for i in range(3):
        if is_sorted_by_asc(arr):
            is_can = True
            break
        arr = get_turn_by_counterclockwise(arr)
    return {'arr': arr, 'is_can': is_can}


def get_turn_by_counterclockwise(arr):
    return [arr[1], arr[2], arr[0]]


def is_sorted_by_asc(arr):
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            return False
    return True
