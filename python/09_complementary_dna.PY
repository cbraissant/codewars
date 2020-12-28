'''
Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells and carries the "instructions" for the development and functioning of living organisms.

If you want to know more http://en.wikipedia.org/wiki/DNA

In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". You have function with one side of the DNA (string, except for Haskell); you need to get the other complementary side. DNA strand is never empty or there is no DNA at all (again, except for Haskell).

More similar exercise are found here http://rosalind.info/problems/list-view/ (source)

DNA_strand ("ATTGC") # return "TAACG"

DNA_strand ("GTAT") # return "CATA"
'''


def DNA_strand(dna):
    '''
    - create a conversion table
    - find the conversion for each character
    '''
    switch = {
        'A': 'T',
        'T': 'A',
        'C': 'G',
        'G': 'C'
    }
    return ''.join(map(switch.get, dna))


def DNA_strand(dna):
    '''
    - same using a for loop
    '''
    switch = {
        'A': 'T',
        'T': 'A',
        'C': 'G',
        'G': 'C'
    }
    return ''.join(switch[x] for x in dna)


def DNA_strand(dna):
    '''
    - translate method
    '''
    return dna.translate(str.maketrans("ATCG", "TAGC"))


if __name__ == "__main__":
    print(DNA_strand('ATTGC'))
