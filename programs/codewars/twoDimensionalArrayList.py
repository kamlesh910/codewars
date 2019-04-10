def matrix_addition(a, b):
    return [[sum(x) for x in zip(a[i], b[i])] for i in range(len(a))]
