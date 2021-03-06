##Parse blastoutput files to get hits with greater than 80 coverage and 30 pident
import argparse
import sys


parse = argparse.ArgumentParser()

#Specify input and output files on the command line
parse.add_argument("--blastout", "-in",type=str,help="name of the blastoutput file to be parsed",required=True)
parse.add_argument("--blastparse", "-out",type=str,help="name of the blast parsed file to write to",required=True)

args = parse.parse_args()



mincover = 80
min_pident = 30
#Open blast output file, and blast parse file to write to
with open(args.blastout) as f, open(args.blastparse, 'w') as outF:
    for line in f:
        lines = line.split('\t')
        query_ID = lines[0]
        hit_ID = lines[1]
        evalue = lines[2]
        pident = lines[3]
        query_start = lines[5]
        query_end = lines[6]
        sub_start = lines[-3]
        sub_end = lines[-2]
        #Calculate covergae from query and subject start and end hits/len of gene
        cover_que = 100 * (int(lines[6])-int(lines[5])) / int(lines[7])
        cover_sub = 100.0 * (int(lines[9])-int(lines[8])) / int(lines[10])
        #Create variable of wanted values for coverage and percent identity
        wanted_values = (cover_que >= mincover) and (cover_sub > mincover) and (float(pident) >= float(min_pident))
        #If wanted values are satisfied, write the BLAST result to file
        if wanted_values:
            outF.write(str(query_ID) + '\t' + str(hit_ID) + '\t'  + str(query_start) + '\t' + str(query_end) + '\t' + str(sub_start) + '\t' + str(sub_end) + '\t' + str(cover_que) + '\t' + str(cover_sub) + '\n')
