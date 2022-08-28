def SumOfThe(N, data):
    for i in range(N):
        number = data[i]
        sum = 0
        for j in range(N):
            if i != j:
                sum += data[j]
        if sum == number:
            return number
