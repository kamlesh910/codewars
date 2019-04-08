def warn_the_sheep(queue):
    print(queue)
    queue=queue[::-1]
    toreturn=""
    if(queue[0]=='wolf'):
        toreturn="Pls go away and stop eating my sheep"
    else:
        toreturn = "Oi! Sheep number {0}! You are about to be eaten by a wolf!".format(queue.index("wolf"))
    return toreturn