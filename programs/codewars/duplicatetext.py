def duplicate_count(text):
    print(text)
    return len(set([i for i in text.lower() if text.lower().count(i)>1]))
     
