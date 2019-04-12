def xo(s):
    if len([s[i] for i in range(len(s)) if s[i].lower()=='x']) == len([s[i] for i in range(len(s)) if s[i].lower()=='o']):
        return True
    else:
        return False
