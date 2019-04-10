import math
def is_square(integer):
    if integer < 0 :
       return False
    root = math.sqrt(integer)
    if int(root) ** 2 != integer: 
        return False
    else:
        return True
