









# Open the fasta file
seqBR=open("BRACA.fasta","r")

# Read the sequence line wise
seq=seqBR.readlines()

# Close the file
seqBR.close()

# Set counters for each base
countA=0
countG=0
countT=0
countC=0

# Eliminate the description line
for lines in seq:
    if lines[0]!=">":

        # For each base type increment the counter by 1 when found one
        for bases in lines:
            if bases=="A":
                countA+=1
            elif bases=="G":
                countG+=1
            elif bases=="T":
                countT+=1
            elif bases=="C":
                countC+=1

# Output the final counts
print("Count of Adenine")
print(countA)
print("Count of Guanine")
print(countG)
print("Count of Thymine")
print(countT)
print("Count of Cytosine")
print(countC)

