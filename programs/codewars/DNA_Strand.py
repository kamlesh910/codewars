def DNA_strand(dna):
    print(dna)
    dna=list(dna)
    for i in range(len(dna)):
        if dna[i]=='A':
            dna[i]='T'
        elif dna[i]=='T':
            dna[i]='A'
        elif dna[i]=='G':
            dna[i]='C'
        elif dna[i]=='C':
            dna[i]='G'
    return "".join(dna)
