import os
from subprocess import call as unix
import glob
from collections import defaultdict
import json, ast
from ete3 import NCBITaxa
import pandas as pd
ncbi = NCBITaxa()

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

ENS2OMA = dict()
with open('OMA_2_latinID.txt') as f2:
    for line in f2:
        lines = line.split('\t')
        OMA_ID = lines[0].strip()
        ENS_ID = lines[1].strip()
        ENS2OMA[ENS_ID] = OMA_ID

OMA2ncbiID = dict()
for k, v in taxa2ncbiID.items():
    OMA = ENS2OMA[k]
    OMA2ncbiID[OMA] = v


confirmed_fams = []
confirmed_FamGenes = defaultdict(list)
for my_file in glob.glob("Confirmed*"):
    with open(my_file) as f:
        for line in f:
            lines = line.split('\t')
            famID = lines[0]
            geneID = lines[1]
            OMA_ID = geneID[:5]
            confirmed_fams.append(famID)
            if OMA_ID in confirmed_FamGenes[famID]:
                continue
            else:
                confirmed_FamGenes[famID].append(OMA_ID)
    

                
with open('/data1/bspm/shortRead_mapping/raw/ambig_dicts/allcomps_dict_sp_ambig.json') as f2:
    my_dict = json.load(f2)

full_dict = ast.literal_eval(json.dumps(my_dict))

#Create dictionary of the confirmed Comp Fams and the full set of genes (taxa IDs) that are in each family as defined by CompositeSearch                                       
confirmed_allGenes_fams_dict = defaultdict(list)
for k, v in full_dict.items():
    if k in set(confirmed_fams):
        for ID in v:
            if ID[:5] in confirmed_allGenes_fams_dict[k]:
                continue
            else:
                confirmed_allGenes_fams_dict[k].append(ID[:5])
    else:
        continue



confirmFamID_ncbiIDs = defaultdict(list)
for famID, IDs in confirmed_allGenes_fams_dict.items():
    for ID in IDs:
        ncbiID = OMA2ncbiID[ID]
        confirmFamID_ncbiIDs[famID].append(ncbiID)


fam_commonAncestorNode = defaultdict(list)
for fam, ncbis in confirmFamID_ncbiIDs.items():
    ncbi_list = []
    ncbi_ancestor_list = []
    taxa_list = []
    node_list = []
    for ID in ncbis:
        ncbiTaxa = str(ncbiID2taxa[ID])
        taxa_list.append(ncbiTaxa)
        ncbiID = int(ID)
        ncbi_list.append(ncbiID)
        ncbi_ancestor_list.append(ID)
    tree = ncbi.get_topology(ncbi_list)
    taxa_tree = tree.get_ascii(attributes=["sci_name"])
    ancestor = tree.get_common_ancestor(ncbi_ancestor_list)
    for node in tree.traverse("levelorder"):
        node_list.append(node.sci_name)
    MRCA_node = node_list[0]
    fam_commonAncestorNode[MRCA_node].append(fam)

MRCA_dict = ast.literal_eval(json.dumps(fam_commonAncestorNode))
final_dict = dict()
for k, v in MRCA_dict.items():
    famCount = len(v)
    final_dict[k] = famCount
    
df = pd.DataFrame(final_dict, index=[0])
sorted_df = df.sort_values(df.last_valid_index(), axis=1)
print(sorted_df)
sorted_df.to_csv('fam_nodeCount.csv', index=False)

#    print(tree.get_ascii(attributes=["sci_name"]))

#tree = ncbi.get_topology([7165, 283909, 9361, 7227, 225164, 9785, 9315, 10090, 7425, 30611, 7757, 9823, 9305, 126957, 32264, 136037])
#tree = fiona.get_topology([9606, 9598, 10090, 7707, 8782])
#print(peter.get_ascii(attributes=["sci_name"]))
