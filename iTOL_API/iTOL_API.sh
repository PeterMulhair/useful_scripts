#$ -cwd
#$ -V
#$ -P omics
#$ -l h_rt=48:00:00
#$ -l h_vmem=20G
#$ -t 1-157
#$ -tc 20

source activate my_root

CMD=$(awk "NR==$SGE_TASK_ID" cmds_iToL.txt)
eval $CMD
