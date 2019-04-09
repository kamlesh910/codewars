def divisible_by(numbers, divisor):
    emptyList=[]
    for number in numbers:    
        if(number%divisor==0):
            emptyList.append(number)
    return emptyList