import itertools

def answer(x, y, z):
    month_days = {1: 31,
                  2: 28,
                  3: 31,
                  4: 30,
                  5: 31,
                  6: 30,
                  7: 31,
                  8: 31,
                  9: 30,
                  10: 31,
                  11: 30,
                  12: 31}
    MONTH = 0
    DAY = 1
    YEAR = 2

    valid_combinations = set()
    permutations = itertools.permutations([x, y, z])

    for permutation in permutations:
        month = permutation[MONTH]
        day = permutation[DAY]
        if month <= 12 and day <= month_days.get(month):
            valid_combinations.add(permutation)

    if len(valid_combinations) > 1:
        return "Ambiguous"
    else:
        return "%02d/%02d/%02d" % valid_combinations.pop()
