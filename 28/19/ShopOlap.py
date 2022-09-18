def ShopOLAP(N, items):
    goods = {}
    for i in range(N):
        [good, count] = items[i].split(' ')
        count = int(count)
        if good not in goods:
            goods[good] = 0
        goods[good] += count
    sorted_goods = sorted(goods.items(), key=lambda item: (-item[1], item[0]))
    arr = []
    for good in sorted_goods:
        arr.append(f'{good[0]} {good[1]}')
    return arr
