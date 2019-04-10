def toJadenCase(string):
    return " ".join([x[0].upper()+x[1:].lower() for x in string.split()])
