# Get broader GO terms & functions for a set of genes

From a list of specific GO terms, get their broader functional parent GO terms from the QuickGO API

* Details on the different GO datasets and how to use the API can be found at [QuickGO API](https://www.ebi.ac.uk/QuickGO/api/index.html#/)

* Within the Gene Ontology database there is a hierarchy of functions, from broad functions to more specific ones. With a set of specific GO terms it may be hard to interpret. This pipeline gets broad GO terms for a set of genes which may be more manageable.

---

**Step 1**

**quickGO_broad_GOcategories.py**

Given a starting dictionary of gene IDs to their specific GO IDs `gene_BP_GOIDs.json`, in order to find more broad functional patterms use the following Python script to find second and third tier gene functions

`python quickGO_broad_GOcategories.py --geneGOs gene_BP_GOIDs.json`

The argument `--geneGOs` requires the name of the dictionary with gene names and specific GO terms (in this case called `gene_BP_GOIDs.json`)

---

**Step 2**

**quickGO_funcSearch.py**

This produces a dictionary in `.json` format of the specific GO term to its more broad GO IDs (Note: there may be multiple broad GO IDs for a single gene)

From this dictionary we can then create a dictionary of each of the broad GO IDs to their functions, using the python script

`python quickGO_funcSearch.py`

---

**Step 3**

**gene_broadFuncs.py**

Finally, using the previous dictionaries we can create a text file of the gene IDs to their broad functions, using the script

`python gene_broadFuncs.py --geneGOs gene_BP_GOIDs.json`

This produces a tab delimited file of the gene ID to its broad functions (which are separated by commas)