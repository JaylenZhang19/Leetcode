def fresh_promotion(code, shopping):
    i, j = 0, 0
    while i < len(code) and j + len(code[i]) <= len(shopping):
        flag = True
        for index, c in enumerate(code[i]):
            if c != 'anything' and c != shopping[j + index]:
                flag = False
        if flag:
            j += len(code[i])
            i += 1
        else:
            j += 1
    return i == len(code)