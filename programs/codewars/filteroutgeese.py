geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]

def goose_filter(birds):
    for gee in geese:
       if(gee in birds):
          birds.remove(gee)
    return birds