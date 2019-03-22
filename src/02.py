#Module2
trna='AAGGGCTTAGCTTAATTAAAGTGGCTGATTTGCGTTCAGTTGATGCAGAGTGGGGTTTTGCAGTCCTTA' #defining trna as a string  
#CK The trna should be initialized before usage -1

A_count=trna.count('A')
C_count=trna.count('C')
G_count=trna.count('G')
T_count=trna.count('T')


print("The length of the trna sequence is %i" % len (trna), "nucleotides") #showing the total number of bases in the sequences
C_count=trna.count('C') #counting the total number of G's in the trna sequence
G_count=trna.count('G') #counting the total number of C's in the trna sequence
print("There are %d 'G' and %d C's in the trna sequence" % (trna.count('G'),trna.count('C'))) #showing the number of G's and C's in the trna sequence.
GC_percent=(trna.count('G')+trna.count('C'))/len (trna)*100
print("The GC percentage of the trna sequence is %.3f" %GC_percent, "%") #This is the calculation for GC content for the trna sequence

#Exercise_2 Finding the positions of amino acids in a given sequence. 
Amino1_seq="MNKMDLVADVAEKTDLSKAKATEVIDAVFA" #Defining the given amino acid sequence as a string.
print("The first amino acid in the sequence is",  Amino1_seq[0]) #Printing output for the first amino acid in the sequence.
print("The fifth amino acid in the sequence is", Amino1_seq[4]) #Printing output for the second amino acid in the sequence.
print("The last amino acid in the sequence is ", Amino1_seq[len (Amino1_seq)-1]) #Printing output for the last amino acid in the sequence.
print("The 'MDL' motif is found at index " , Amino1_seq.find("MDL"))

DNA1_seq="AAAAATCCCGAGGCGGCTATATAGGGCTCCGGAGGCGTAATATAAAA"
print ("'TCCGGA'restriction site is at index %d to" % DNA1_seq.find("TCCGGA"),\
       DNA1_seq.find("TCCGGA")+len ("TCCGGA"), "of the given DNA sequence")
       # Try and figure out how many times the restriction site is repeated.
       

