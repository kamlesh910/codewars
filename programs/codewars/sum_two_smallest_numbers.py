def sum_two_smallest_numbers(numbers):
    minnumber1=min(numbers)
    numbers.remove(min(numbers))
    minnumber2=min(numbers)
    return minnumber1+minnumber2
