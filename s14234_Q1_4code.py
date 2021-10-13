# Import and open the fasta file into python

BRseq=open("BRACA.fasta","r")

# read it line by line

seq=BRseq.readlines()

# close the fasta file

BRseq.close()

# set a counter

count=0

# for the read count the number of characters in the read one by one

for line in seq:

    # Remove the description line
    if line[0]!=">":

        # count character 1 by 1
        for i in line:
            if i!="\n":
                count += 1

# output the final length
print(count)


