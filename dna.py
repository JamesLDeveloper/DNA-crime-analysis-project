sample = ['GTA','GGG','CAC']

def read_dna(dna_file):
    dna_data = ""
    with open(dna_file, "r") as f:
        for line in f:
            dna_data += line
    return dna_data

#print read_dna("suspect1.txt") testing reads correctly
#print read_dna("suspect2.txt") testing reads correctly
#print read_dna("suspect3.txt") testing reads correctly

def dna_codons(dna):
    codons = []
    for i in range(0, len(dna), 3):
        if (i + 3) < len(dna):
            codons.append(dna[i:i+3])
    return codons

#print dna_codons(read_dna("suspect1.txt")) testing reads correctly
#print dna_codons(read_dna("suspect2.txt")) testing reads correctly
#print dna_codons(read_dna("suspect3.txt")) testing reads correctly

def match_dna(dna):
    matches = 0
    for codon in dna:
        if codon in sample:
            matches += 1
    return matches

#print match_dna(dna_codons(read_dna("Suspect1.txt")))
#print match_dna(dna_codons(read_dna("Suspect2.txt")))
#print match_dna(dna_codons(read_dna("Suspect3.txt")))

def is_criminal(dna_sample):
    dna_data = read_dna(dna_sample)
    codons = dna_codons(dna_data)
    num_matches = match_dna(codons)
    if num_matches >= 3:
        print "Number of matches is: %i, which is significant. Investigation into this suspect should continue." % (num_matches)
    else:
        print "Number of matches is: %i, which is insignificant. Suspect should be released unless more evidence is gathered." % (num_matches)

is_criminal("Suspect1.txt")
is_criminal("Suspect2.txt")
is_criminal("Suspect3.txt")
