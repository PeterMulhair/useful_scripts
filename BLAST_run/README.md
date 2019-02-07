#Run BLAST with preferred parameters in outmft 6

Command to run BLAST in output format 6
* Evalue e-5
* Max_target_seq 5000
* Percent ident, bitscore, and coverage specified can be parsed in output files

```Shell
blastp -query file.fasta -db db_file -evalue 1e-5 -seg yes -soft_masking true -max_target_seqs 5000 -outfmt "6 qseqid sseqid evalue pident bitscore qstart qend qlen sstart send slen" -out file.blastoutput.fa
```