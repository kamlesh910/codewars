def fillable(stock, merch, n):
    print("stock {0}, merch {1}, n {2}".format(stock, merch, n))
    if merch in stock:
        if n<=stock[merch]:
            return True
        else:
            return False
    else:
        return False
