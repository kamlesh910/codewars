def odd_count(n): 
    return len([x for x in range(1, n) if x%2!=0])


def odd_count(n): 
    li=[]
    for x in range(1, n):
        if x%2!=0:
            li.append(x)
    return len(li)        
    
