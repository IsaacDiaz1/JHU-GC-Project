codons = {"UUU":"Phe", "UUC":"Phe", "UUA":"Leu", "UUG":"Leu",
          "UCU":"Ser", "UCC":"Ser", "UCA":"Ser", "UCG":"Ser",
          "UAU":"Tyr", "UAC":"Tyr", "UAA":"STOP", "UAG":"STOP",
          "UGU":"Cys", "UGC":"Cys", "UGA":"STOP", "UGG":"Trp",
          "CUU":"Leu", "CUC":"Leu", "CUA":"Leu", "CUG":"Leu",
          "CCU":"Pro", "CCC":"Pro", "CCA":"Pro", "CCG":"Pro",
          "CAU":"His", "CAC":"His", "CAA":"Gln", "CAG":"Gln",
          "CGU":"Arg", "CGC":"Arg", "CGA":"Arg", "CGG":"Arg",
          "AUU":"Ile", "AUC":"Ile", "AUA":"Ile", "AUG":"Met",
          "ACU":"Thr", "ACC":"Thr", "ACA":"Thr", "ACG":"Thr",
          "AAU":"Asn", "AAC":"Asn", "AAA":"Lys", "AAG":"Lys",
          "AGU":"Ser", "AGC":"Ser", "AGA":"Arg", "AGG":"Arg",
          "GUU":"Val", "GUC":"Val", "GUA":"Val", "GUG":"Val",
          "GCU":"Ala", "GCC":"Ala", "GCA":"Ala", "GCG":"Ala",
          "GAU":"Asp", "GAC":"Asp", "GAA":"Glu", "GAG":"Glu",
          "GGU":"Gly", "GGC":"Gly", "GGA":"Gly", "GGG":"Gly"}
        
def main():
    '''
    Reads and returns the text that contains the DNA. Assigns string to 
    dna varible.
    '''
    dna = readFile('htt.txt')  
    
    '''
    Calls replication function and writes the complementary strand to the 
    replication.txt file.
    '''
    CompStrand = replication(dna)      
    writeFile('replication.txt', CompStrand)
    
    '''
    Calls the restriction function and writes the shortest fragment of the
    DNA into the fragment.txt file after being cut by restriction enzymes.
    '''
    allfrags = restriction(dna, 'CAGCTG')
    smallest_frag = min(allfrags, key=len)
    writeFile('fragment.txt', smallest_frag)
    
    '''
    Calls the mutation function which returns the max number of consecutive
    Gln codons. Then, that max number is analyzed to see if there is a
    higher or lower risk for Huntington's disease.
    '''
    numrepeats = mutation(dna)
    if numrepeats >= 36:
        print('This gene indicates a higher risk of Huntington\'s disease.')
    else:
        print('This gene indicates a lower risk of Huntington\'s disease.')
    
    

def readFile(fileName):
    """
    input: fileName to read
    output: text in file as string
    """
    with open(fileName,'r') as textFile:
        text = textFile.read()
        
    return text.strip()
    
    
def writeFile(fileName,text):
    '''
    input: fileName and text
    output: text is written into the fileName
    '''
    with open(fileName,'w') as textFile:
        textFile.write(text.strip())

    
def replication(dna):
    '''
    This function returns the replicated DNA by looping through each element (bases)
    and concatinating its complementary base to an empty string.Then the new string 
    is wriiten to the replication.txt file.
    '''
    comp_dna = ''
    for i in dna:
        if (i == 'A'):
            comp_dna += 'T'
        elif (i == 'T'):
            comp_dna += 'A'
        elif (i == 'C'):
            comp_dna += 'G'
        elif (i == 'G'):
            comp_dna += 'C'
            
    return comp_dna
    

def restriction(dna, seq): 
    '''
    This function will return fragments in a list of the input DNA. The DNA sequence 
    will be cut at the center of the recognition sequence which will fragment the DNA. 
    The shortest fragment will be written into the fragment.txt file.
    '''
    fragments = []
    fraglist = dna.split(seq)
    fragments.append(fraglist[0] + seq[0:len(seq) // 2])
    
    for i in range(1, len(fraglist)-1):
            fragments.append(seq[len(seq) // 2:] + fraglist[i] + seq[0:len(seq) // 2])
    
    fragments.append(seq[len(seq) // 2:] + fraglist[-1])
        
        
    return fragments

def transcription(dna):
    """
    This function takes in a DNA sequence. Then a for loop is used to cycle through 
    each base pair in the DNA sequence. The loop adds the original bases into the 
    empty string (transcriptedDNA), unless the base is T. The base U will replace T.   
    """
    transcriptedDNA = ''
    
    for base in dna:
        if (base == 'T'):
            transcriptedDNA += 'U'
        else:
            transcriptedDNA += base
            
    return transcriptedDNA #mRNA

def translation(mrna):
    """
    This function takes in mRNA, which is returned by the transcription function.
    The function then compares three bases in the mrna to the codon chart 
    (Dictionary at top), and returns the corresponding codon.    
    """
    aminoacids = ''

    for bases in range(0, len(mrna), 3): 
        for key, value in codons.items():
            if (mrna[bases:bases+3] == key):
                aminoacids += value + ' '
    return aminoacids
    
def mutation(dna):
    """
    This function takes in a DNA string and outputs the max number of times that the Gln amino
    acid is consecutively repeated. This is done by using looping through string with the find 
    function. This will continue to loop until max repetion occurs. This max is returned
    """
    repeats = 1
    
    while dna.find('CAG' * repeats) != -1:
        repeats += 1
        
    
    return repeats - 1

if __name__ == "__main__": main()