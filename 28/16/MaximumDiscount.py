def MaximumDiscount(n, prices):
    if n < 3:
        return 0
    max_things = 3
    max_discount1, max_discount2 = 0, 0
    count_free_things = n // max_things
    prices.sort(reverse=True)
    max_discount1 = sum(prices[-count_free_things:])
    while len(prices) >= max_things:
        max_discount2 += min(prices[:max_things])
        prices = prices[max_things:]
    return max(max_discount1, max_discount2)
