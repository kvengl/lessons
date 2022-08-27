def MadMax(N, Tele):
    if N == 1:
        return Tele;
    sorted_tele = bubble_sort(Tele)
    middle_index = N // 2
    arr = []
    for i in range(middle_index):
        arr.append(sorted_tele[i])
    arr.append(sorted_tele[N - 1])
    for i in range(N - 2, middle_index, -1):
        arr.append(sorted_tele[i])
    arr.append(sorted_tele[middle_index])
    return arr

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr