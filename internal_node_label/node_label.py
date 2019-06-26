#Label internal nodes of newick tree and save to a new tree file
from ete3 import Tree
import argparse

parse = argparse.ArgumentParser()

parse.add_argument("--tree",type=str, required=True)#Input tree to be specified

args = parse.parse_args()

famID = args.tree.split('.')[0]

#Load input tree
tree = Tree(args.tree)

#For each internal node in the tree assign it a label based on the edge number starting from 0 (which is the root)
edge = 0
for node in tree.traverse():
   if not node.is_leaf():
      node.name = "NODE_%d" %edge
      edge += 1

#Write the new labelled tree to a newick file
tree.write(format=8, outfile = famID + "_nodeLabel.nwk")
