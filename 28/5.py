def SynchronizingTables(N, ids, salary):
    sorted_ids = sorted(ids)
    sorted_salary = sorted(salary)
    obj = {}
    for i in range(N):
        obj[sorted_ids[i]] = sorted_salary[i]
    res = []
    for i in range(N):
        res.append(obj[ids[i]])
    return res