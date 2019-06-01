# Get broader GO terms & functions for a set of genes

From a list of specific GO terms, get their broader functional parent GO terms from the QuickGO API

* Details on the different GO datasets and how to use the API can be found at [QuickGO API](https://www.ebi.ac.uk/QuickGO/api/index.html#/)

* Within the Gene Ontology database there is a hierarchy of functions, from broad functions to more specific ones. Given a starting dictionary of gene IDs to their specific GO IDs `gene_BP_GOIDs.json`, in order to find more broad functional patterns use the Python script to find second and third tier gene functions

`quickGO_broad_GOcategories.py`

---

This produces a dictionary in `.json` format of the specific GO term to its more broad GO IDs (Note: there may be multiple broad GO IDs for a single gene)

From this dictionary we can then create a dictionary of each of the broad GO IDs to their functions, using the python script

`quickGO_funcSearch.py`

---

Finally, using the previous dictionaries we can create a text file of the gene IDs to their broad functions, using the script

`gene_broadFuncs.py`

This produces a tab delimited file of the gene ID to its broad functions (which are separated by commas)