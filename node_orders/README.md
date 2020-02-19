# Get order of internal nodes from a time tree

Given a time calibrated tree with branch lengths and internal node names, get list of nodes ordered based on time from oldest to youngest

Script uses [ete3 python module](http://etetoolkit.org/docs/latest/tutorial/)

```Shell
python tree_parse.py --tree timetree.nwk --outgroup OUTGP
```

Options:
* `--tree`: defines tree with branch lengths and internal node names
* `--outgroup`: name of species outgroup in tree

Example tree `metazoa_timeTree_outgMonBrev_OutG_OMAnames_nodeLabel.nwk`	shows what format the tree should be in