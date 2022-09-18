def ShopOLAP(N, items):
    goods = {}
    for i in range(N):
        [good, count] = items[i].split(' ')
        count = int(count)
        if good not in goods:
            goods[good] = 0
        goods[good] += count
    arr = []
    for good in goods:
        arr.append(f'{good} {goods[good]}')
    sorted_arr = sorted(arr)
    return sorted_arr
