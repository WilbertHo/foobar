# http://oeis.org/wiki/Balanced_ternary_numeral_system
# https://en.wikipedia.org/wiki/Balanced_ternary

def answer(x):
    # convert x to balanced ternary
    n = x
    k = 0
    digits = list()
    while True:
        d = (n % (pow(3, k + 1))) / pow(3, k)
        d = -1 if d == 2 else d
        digits.append(d)
        n = n - d * pow(3, k)
        k += 1
        if n == pow(3, k):
            digits.append(1)
            break
        if n == 0:
            break

    balanced_ternary = [['-', 'R', 'L'][i] for i in digits]
    while balanced_ternary[-1] == '-':
        balanced_ternary.pop(-1)

    return balanced_ternary
