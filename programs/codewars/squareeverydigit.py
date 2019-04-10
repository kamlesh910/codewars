def square_digits(num):
    return int(''.join([str(int(str(num)[i])*int(str(num)[i])) for i in range(len(str(num)))]))
