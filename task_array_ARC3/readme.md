# Running task array on ARC3 HPC


* Given a list of commands where the same code is run on all files at hand (cmds.txt file)

* Run the 500 commands in groups of 50 at one time

`#$ -cwd
#$ -V
#$ -P omics
#$ -l h_rt=48:00:00
#$ -l h_vmem=20G
#$ -t 1-500
#$ -tc 50


CMD=$(awk "NR==$SGE_TASK_ID" cmds.txt)
eval $CMD`

---