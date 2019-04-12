def high_and_low(numbers):
    return '{0} {1}'.format(max([int(x) for x in numbers.split()]),min([int(x) for x in numbers.split()]))
    
