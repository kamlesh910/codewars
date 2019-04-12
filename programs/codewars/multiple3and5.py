def solution(number):
    print(number)
    suml=[]
    for i in range(1,number):
        if(3*i<number):
            suml.append(3*i)
        if(5*i<number):
            suml.append(5*i)
    print(list(set(suml)))
    return sum(list(set(suml)))
    
  
