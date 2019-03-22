#Module_6 Calculating GC content using my function and validating DNA using my own function
def DNA_Validity(seq):
    valid=['A','T','C','G']
    ifValid = True
    for base in seq:
        if base not in valid:
            ifValid=ifValid and False ##CK: Jyust needed: ifValid = False -1
        else:
            ifValid=ifValid and True ##CK: The else block wouldn't really be necessary
    return ifValid
#Function describing my function for calculating GC. Checking DNA validity too. If an invalid sequence is used the message invalid DNA will pop up.
def percentageGC(seq):
    if DNA_Validity(seq):
        percentage=(seq.count('G')+seq.count('C'))/len (seq)*100
        print(percentage) #this message should be informative -1 
    else:
        print("Invalid DNA")
yourdna = "GACTAGTAGTACTGATAACCCTTGT"
percentageGC(yourdna) #This function should calculate the GC percentage and Check the validity of your DNA. 
#CK You need to provide yourdna -1
    

