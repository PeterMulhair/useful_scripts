# Obtaining a species tree given a list of taxa

Notebook showing how to use `ete3` and the EBI taxonomy API

* From a list of species names, create a tree showing the names of all taxa and internal nodes

* Two example scripts `speciesTree_interalNodes.py` and `internalNode_Trees.py` showing (1) how to get an internally labelled species tree from a list of taxa and (2) how to get labelled species tree and LCA node name for multiple gene families at once

---

Import ete3

```Shell
from ete3 import NCBITaxa
ncbi = NCBITaxa()
```

