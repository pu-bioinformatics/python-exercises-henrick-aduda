#Module4
##Use lists to reverse the string above.
### Then find a good way to replace A to T and and C to G . Give the output of the complement
DNA_seq=list('AAAAATCCCGAGGCGGCTATATAGGGCTCCGGAGGCGTAATATAAAA') #Declaring the given sequence as a list .
DNA_seq.reverse()#reversing the given sequence
print ("This is the reverse string of the given DNA sequence=",'' .join (DNA_seq))# Printing the output of the reverse sequence

DNA="AAAATATAATGCGGAGGCCTCGGGATATATCGGCGGAGCCCTAAAAA" #Declaring the reverse sequence as a string so as to come up with a complement using string.replace feature
#CK: By declaring a new DNA sequence,  you only end up with the DNA complement, but notreversed. -2
DNA= DNA.replace('A','t')# Using replace feature to give complement of the bases
DNA=DNA.replace('C','g')
DNA=DNA.replace('G','c')
DNA=DNA.replace('T','a')
print("This is the reverse complement of the given DNA sequence %s" %DNA.upper())#Printing the output of the reverse complement




