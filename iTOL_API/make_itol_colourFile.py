##Script to create the .itol.colourstrips.txt files required if you wish to colour certain branches on the tree
from Bio import SeqIO
import glob

#Create a list of the species/gene IDs you wish to label from a text file of said IDs
label_list = []
with open('label_IDs.txt') as f:
    for line in f:
        ID = line.strip()
        label_list.append(ID)

#Allocate the branch label colour (red here)
label_colour = "#d73027"

#For fasta from which the newick tree was made, create a colour file (used for the --colour parameter in the iTOL_API.py)
for my_file in glob.glob("*fasta"):
    files = my_file.split('/')[-1]
    fasta_name = files.split(".")[0]
    with open(my_file) as f, open(fasta_name + ".itol.colourstrips.txt", "w") as outF:
        outF.write("DATASET_COLORSTRIP\nSEPARATOR TAB\nCOLOR_BRANCHES\t1\nDATASET_LABEL\tcolors_annotation\nCOLOR\t#d73027\nDATA\n")
        for record in SeqIO.parse(f, "fasta"):
            header = record.description
            ID = record.id
            if ID in label_list:
                outF.write(ID + "\t" + label_colour + "\n")
