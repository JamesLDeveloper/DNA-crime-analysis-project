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



