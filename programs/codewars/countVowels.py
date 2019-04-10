def getCount(inputStr):
    return sum([inputStr.lower().count(x) for x in "aeiou"])
