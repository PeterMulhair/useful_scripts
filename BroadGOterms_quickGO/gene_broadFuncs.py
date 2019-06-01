#From the original dictionary of gene IDs to specific GO terms, use the newly created dictionaries to create a text file of the genes to their broad functions
import json
from collections import defaultdict

#Open the gene to specific GO ID dictionary 
with open('gene_BP_GOIDs.json') as f:
    compGene_specGOs = json.load(f)

#Open the specific GO ID to broad GO IDs dictionary 
with open('specGO_2_broadGO_BP.json') as f:
    specGO_broadGO = json.load(f) 

#Open the broad GO ID to function dictionary
with open('broadGO_functions_BP.json') as f:
    broadGO_func = json.load(f) 

count = 0
compGene_broadGOs = []
compGene_functions = []
gene_broadFunctions = defaultdict(list)
for k, v in compGene_specGOs.items():#For each gene and specific GO ID
    GOID = 'GO:' + v
    try:
        geneBroadGO = specGO_broadGO[GOID]#Find the broad GO IDs
        for ID in set(geneBroadGO):
            compGene_broadGOs.append(ID)
            func = broadGO_func[ID]#Find the broad functions
            
            if func in gene_broadFunctions[k]:
                continue
            else:
                gene_broadFunctions[k].append(func)#Create a dictionary of gene IDs to their broad functions

    except:
        count+=1
        continue

#Write the geneID and its broad functions to a tab delimited file, with functions separated by commas
with open('compGene_broadFunctions.tsv', 'w') as outF:
    for gene, funcs in gene_broadFunctions.items():
        outF.write(gene + '\t')
        for fun in funcs:
            outF.write(fun + ',')
        outF.write('\n')


print(count, 'out of', len(compGene_specGOs), 'genes have a single annotated function')





#print('\n')

#print(Counter(compGene_functions))
#print('\n')

#print(len(compGene_broadGOs))
