def points(games):
    print(games)
    sum=0
    for point in games:
        x,y=point.split(":")
        if(x>y):
            sum+=3
        elif(x<y):
            sum+=0
        elif(x==y):
            sum+=1            
    return sum