def find_it(seq):
    for letter in set(seq):
        if(seq.count(letter)%2!=0):
            return letter
        
