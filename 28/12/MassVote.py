def MassVote(n, votes):
    all_votes = sum(votes)
    if n == 1:
        return 'majority winner 1'

    index_max = 0
    prev_index_max = 0
    for i in range(n):
        if votes[i] >= votes[index_max]:
            if i == 0:
                prev_index_max = 1
            else:
                prev_index_max = index_max
            index_max = i
        elif votes[i] > votes[prev_index_max]:
            prev_index_max = i

    part1 = votes[index_max] * 100 / all_votes
    part2 = votes[prev_index_max] * 100 / all_votes

    if part1 > 50:
        return f'majority winner {index_max + 1}'
    if 50 >= part2 != part1:
        return f'minority winner {index_max + 1}'

    return 'no winner'
