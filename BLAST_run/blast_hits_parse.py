import glob
from Bio import SeqIO

#Open the genome file that you want to pull the blast hit sequence from and create dictionary of geneID to its sequence
geneID2seq = dict()
with open('genome.fasta') as genome:
    for record in SeqIO.parse(genome, 'fasta'):
        fasta_header = record.description
        geneID = record.id
        seq = str(record.seq)
        geneID2seq[geneID] = seq

#Loop through each blastparsed file
for my_file in glob.glob("*.blastparse"):
    geneName = my_file.split('.')[0]
    #Open new files for the reciprocal BLAST sequences
    with open(my_file) as f, open(geneName + '.recipBlast.fasta', 'w') as outF:
        for line in f:
            lines = line.split('\t')
            #blast_hit is the gene id from the genome that had a hit
            blast_hit = lines[1]
            #get the sequence for that gene from the above dictionary
            blast_hit_seq = geneID2seq[blast_hit]
            #Write the blast hit gene ID and its sequence to the recip file in fasta format
            outF.write(">" + blast_hit + "\n" + blast_hit_seq + "\n")
