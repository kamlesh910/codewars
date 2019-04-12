def spin_words(sentence):
    eli=[]
    for word in sentence.split():
        if len(word)>4:
            eli.append(word[::-1])
        else:
            eli.append(word)
    return ' '.join(eli)
            
