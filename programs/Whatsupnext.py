def next_item(xs, item):
    if item not in xs:
        return None
        for item in xs:        
            elif(xs.index(item)==len(xs)-1):
                print("01 index {0}".format(xs.index(item)))  
                return None
            else:
                index=xs.index(item)
                print("02 index {0}".format(xs[index+1]))
    return xs[index+1]