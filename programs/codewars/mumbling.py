def accum(s):
    str=''
    for i in range(len(s)):
        str+=s[i].upper()
        for j in range(i):
            str+=s[i].lower()
        str+='-'
    return str[:-1]
