import glob
from Bio import SeqIO

#Open the genome file that you want to pull the blast hit sequence from 
with open('genome.fasta') as genome:
    for record in SeqIO.parse(genome, 'fasta'):
        fasta_header = record.description
        geneID = record.id
        seq = str(seq)

    #Loop through each blastparsed file
    for my_file in glob.glob("*.blastparse"):
        geneName = my_file.split('.')[0]
        #Open new files for the reciprocal BLAST sequences
        with open(my_file) as f, open(geneName + '.recipBlast.fasta', 'w') as outF:
            for line in f:
                lines = line.split('\t')
                #Gene id from the genome that had a hit
                blast_hit = lines[1]
                if blast_hit == geneID:
                    #if the blast hit matches a geneID in the genome write the geneID and sequence to the recip file
                    outF.write(">" + geneID + "\n" + seq + "\n")
