def in_array(array1, array2):
    getRet=[]
    for a1 in array1:
        for a2 in array2:
            if a1 in a2:
                getRet.append(a1)                
    return sorted(list(set(getRet)))