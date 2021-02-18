def proteins(strand):

    protein_list = []

    for condon in split_strings(strand):
        protein = translation_pairs.get(condon)
        if not protein or protein == 'STOP':
            return protein_list
        else:
            protein_list.append(protein)
    return protein_list

translation_pairs = {
    "AUG" : "Methionine",
    "UUU" : "Phenylalanine",
    "UUC" : "Phenylalanine",
    "UUA" : "Leucine",
    "UUG" : "Leucine",
    "UCU" : "Serine",
    "UCG" : "Serine",
    "UCA" : "Serine",
    "UCC" : "Serine",
    "UAU" : "Tyrosine",
    "UAC" : "Tyrosine",
    "UGU" : "Cysteine",
    "UGC" : "Cysteine",
    "UGG" : "Tryptophan",
    "UAA" : "STOP",
    "UGA" : "STOP",
    "UAG" : "STOP"
}

def split_strings(string):
    split_len = 3
    return [string[i * split_len:i * split_len + split_len] for i in range(int(len(string) / split_len))]
