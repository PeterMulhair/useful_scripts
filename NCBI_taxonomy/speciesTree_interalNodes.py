import os
from subprocess import call as unix
import glob
from collections import defaultdict
import json, ast
from ete3 import NCBITaxa
import pandas as pd
ncbi = NCBITaxa()

#Create dictionary of taxa latin name to ncbi format latin name
taxa2ncbiID = dict()
ncbiID2taxa = dict()
with open('tax_report.txt') as f:
    next(f)
    next(f)
    for line in f:
        lines = line.split('|')
        taxa = lines[1].strip()
        ncbiTaxa = lines[2].strip()
        ID = lines[-1].strip()
        taxa2ncbiID[taxa] = ID
        ncbiID2taxa[ID] = ncbiTaxa

#Create dictionary of OMA ID to ncbi format latin name
ENS2OMA = dict()
with open('OMA_2_latinID.txt') as f2:
    for line in f2:
        lines = line.split('\t')
        OMA_ID = lines[0].strip()
        ENS_ID = lines[1].strip()
        ENS2OMA[ENS_ID] = OMA_ID

#Create dictionary of OMA ID to ncbi taxa number
OMA2ncbiID = dict()
for k, v in taxa2ncbiID.items():
    OMA = ENS2OMA[k]
    OMA2ncbiID[OMA] = v

#Create list of the ncbi number IDs in the dataset
ncbi_list = []
for IDs in OMA2ncbiID.values():
    ncbi_list.append(IDs)

#From the list of ncbi IDs, create a tree with all internal nodes labelled
node_list = []    
tree = ncbi.get_topology(ncbi_list)
print(tree.get_ascii(attributes=['sci_name']))

#Create list of all taxa and internal node names
for node in tree.traverse("levelorder"):
    node_list.append(node.sci_name)
print(node_list)

