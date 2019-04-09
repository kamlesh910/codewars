def stray(arr): 
    rchar=0
    for a in list(set(arr)):
        if(arr.count(a)==1):
            rchar=a
    return rchar
      
    