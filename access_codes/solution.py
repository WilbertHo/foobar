def answer(x):
    codes = list()
    for code in x:
        if code not in codes and code[::-1] not in codes:
            codes.append(code)

    return len(codes)
