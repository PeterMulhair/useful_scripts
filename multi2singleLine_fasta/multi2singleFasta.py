import glob
from Bio import SeqIO

#For each fasta file in a dir
for my_file in glob.glob("*.fasta"):
    file_name = my_filefiles.split(".all")[0]
    #Open a new file for single line versions of the fastas
    with open(my_file) as f, open(file_name + '.1line.fa', 'w') as outF:
        #Use SeqIO to get a single lined str of the sequence
        for record in SeqIO.parse(f, 'fasta'):
            header = record.description
            seq = str(record.seq)
            outF.write(header + '\n' + seq + '\n')
