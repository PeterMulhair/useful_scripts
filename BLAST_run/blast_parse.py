#Parse blastoutput files to get hits with greater than 80 coverage

taxa_count = 0
mincover = 80
blast_hits = []
with open('../data/results/blast_output/' + k + '_blast.fasta.blastoutput') as f2:
    for line in f2:
        lines = line.split('\t')
        hit_ID = lines[1]
        evalue = lines[2]
        query_start = lines[5]
        query_end = lines[6]
        sub_start = lines[-3]
        sub_end = lines[-2]
        cover_que = 100 * (int(lines[6])-int(lines[5])) / int(lines[7])
        cover_sub = 100.0 * (int(lines[9])-int(lines[8])) / int(lines[10])
        wanted_values = (cover_que >= mincover) and (cover_sub > mincover)
        if wanted_values:
            taxa_count += 1
            blast_hits.extend((hit_ID, query_start, query_end, cover_que, cover_sub, '\n'))
