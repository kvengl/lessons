def PatternUnlock(N, hits):
    numbers_location_in_matrix = {
        1: [0, 1],
        2: [1, 1],
        3: [2, 1],
        4: [2, 0],
        5: [1, 0],
        6: [0, 0],
        7: [2, 2],
        8: [1, 2],
        9: [0, 2]
    }

    def get_distance_between_points(p1, p2):
        location1 = numbers_location_in_matrix[p1]
        location2 = numbers_location_in_matrix[p2]
        if location1[0] == location2[0] or location1[1] == location2[1]:
            return 1
        return 2 ** 0.5

    def get_distance():
        distance = 0
        for i in range(0, N - 1):
            distance += get_distance_between_points(hits[i], hits[i + 1])
        return distance

    def normalize_distance(distance):
        distance = float('{:.5f}'.format(distance))
        distance = str(distance)
        new_distance = ""
        for i in distance:
            if i != '0' and i != '.':
                new_distance += i
        return new_distance

    distance = get_distance()
    distance = normalize_distance(distance)
    return distance