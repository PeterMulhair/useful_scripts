#!/usr/bin/python3
from ete3 import Tree
import argparse

'''
Given a species tree with branch lengths and internal 
nodes labelled get ordered list of nodes based on age
'''

parse = argparse.ArgumentParser()

parse.add_argument("--tree",type=str, help="name of tree file with branch lengths and internal node names",required=True)
parse.add_argument("--outgroup",type=str, help="name of outgroup species name in tree",required=True)

args = parse.parse_args()


#Load tree
t = Tree(args.tree, format=1)#Format 1 loads tree with branch lengths and internal node names
print('Loading tree...' + '\n' + 'Make sure your tree has branch lengths and internal node names')

#Traverse the tree to get a list of internal and tip node names
nodes1 = []
for node in t.traverse("levelorder"):
    nodes1.append(node.name)


#outgroup = str(args.outgroup)

#For each node in the tree get the distance from that node to the outgroup tip node, create a dictionary of this information for each node in the tree
node_age_dict = {}
for node in t.traverse("levelorder"):
    node_name = node.name
    node = t&node.name
    node_age = node.get_distance(args.outgroup)
    node_age_dict[node_name] = node_age

#Sorted the dictionary of node name to node age from oldest to youngest
sorted_dict = {k: v for k, v in sorted(node_age_dict.items(), key=lambda item: item[1])}


#Create list of sorted node names based on age of node
sorted_nodes = []
for k, v in sorted_dict.items():
    sorted_nodes.append(k)

#Write the ordered list of nodes based on age to outfile (optional)
with open('node_age_sorted.txt', 'w') as outF:
    for node in sorted_nodes[2:]:#Skip outgroup and root nodes
        outF.write(node + '\n')
