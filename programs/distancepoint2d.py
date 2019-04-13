import math
def distance_between_points(a, b):
    print(a.x,a.y,b.x,b.y)
    print(math.sqrt((a.x-b.x)*(a.x-b.x)+(a.y-b.y)*(a.y-b.y)))
    return math.sqrt((a.x-b.x)*(a.x-b.x)+(a.y-b.y)*(a.y-b.y))
    
