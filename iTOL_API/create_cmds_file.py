#Create the cmds.txt file to run multiple jobs in a task array on ARC3
import glob

with open('cmds_iToL.txt', 'w') as outF:
    for tree_file in glob.glob("*.nwk"):#For each of your newick tree files (with extension .nwk)
        file_ID = tree_file.split('.')[0]
        outF.write("python iTOL_API.py --tree " + file_ID + ".nwk  --colour " + file_ID + ".itol.colourstrips.txt" + '\n')
