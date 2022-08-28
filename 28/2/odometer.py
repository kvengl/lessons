def odometer(oksana):
    distance = 0
    prev_time = 0
    for i in range(0, len(oksana), 2):
        if i + 1 < len(oksana):
            time_from_start = oksana[i + 1]
        else:
            break
        time = time_from_start - prev_time
        prev_time = time_from_start
        speed = oksana[i]
        distance += speed * time
    return distance
