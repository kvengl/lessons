def LineAnalysis(line):
    if len(line) == 1:
        return True
    middle = len(line) // 2
    return line[0:middle] == line[-middle:][::-1]
