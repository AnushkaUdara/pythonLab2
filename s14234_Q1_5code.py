

#Open and import fasta file

BRseq=open("BRACA.fasta","r")

#read the file linewise

seq=BRseq.readlines()

#close the file

BRseq.close()

#define a string variable to receive the string sequences
totalBases=""

#eleminate the definition line
for lines in seq:
    if lines[0]!=">":

        #eleminate the escape sequances
        for bases in lines:
            if bases!="\n":

                #add sequance to the string
                totalBases+=bases

#output the length of the sequance
print(len(totalBases))


