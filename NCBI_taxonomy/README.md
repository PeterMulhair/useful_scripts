# Obtaining a species tree given a list of taxa

Notebook showing how to use `ete3` and the EBI taxonomy API to obtain internally labelled species tree

* Details on how to use full taxonomy API can be found at [NCBITaxa tutorial](http://etetoolkit.org/docs/latest/tutorial/tutorial_ncbitaxonomy.html)

* From a list of species names, create a tree showing the names of all taxa and internal nodes


* Attached two example scripts `speciesTree_interalNodes.py` and `internalNode_Trees.py` showing (1) how to get an internally labelled species tree from a list of taxa and (2) how to get labelled species tree and LCA node name for multiple gene families at once


---

Import `NCBITaxa`

```Shell
from ete3 import NCBITaxa
ncbi = NCBITaxa()
```

Given a list of species names:

```Shell
amphimedon queenslandica
caenorhabditis elegans
drosophila melanogaster
danio rerio
gallus gallus
ornithorhynchus anatinus
sus scrofa
homo sapien
```


* Get NCBITaxa ID from [NCBI Taxonomy Browser](https://www.ncbi.nlm.nih.gov/Taxonomy/TaxIdentifier/tax_identifier.cgi) (file saved as `tax_report.txt`)


From the list of number IDs in `tax_report.txt` create and print internally labelled tree

```Shell
tree = ncbi.get_topology(ncbi_list)
print(tree.get_ascii(attributes=['sci_name']))
```

Create list of all labelled nodes in the tree

```Shell
node_list = []
for node in tree.traverse("levelorder"):
    node_list.append(node.sci_name)
```
