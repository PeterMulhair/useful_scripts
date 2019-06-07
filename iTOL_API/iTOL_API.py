'''
This is an example script for using itol.py
To use itol.py, you essentially have to instantiate the object, set the tree,
submit the file to itol, then use the returned data
'''

import os
import sys
import argparse

parse = argparse.ArgumentParser()

#arguments for tree file choice
parse.add_argument("--tree",type=str,help="name of the tree of interest",required=True)#Tree of interest
parse.add_argument("--colour",type=str,help="name of the tree colour file",required=True)


args = parse.parse_args()

chosentree = args.tree

family_domain_ID = args.tree.split(".")[0]

current_dir = os.path.dirname(os.path.realpath(__file__))
root_path = os.path.join(current_dir, '..')
sys.path.append(root_path)

from itolapi import Itol, ItolExport  # NOQA

print('Running example itol and itolexport script')
print('')
print('Creating the upload params')

# Create the Itol class
test = Itol()

# Set the tree file
tree = os.path.join(current_dir, args.tree)
test.add_file(tree)
test.add_file(os.path.join(current_dir, args.colour))
#test.add_file(os.path.join(current_dir, 'labels.txt'))
#test.add_file(os.path.join(current_dir, 'ranges.txt'))
# Add parameters
test.params['treeName'] = 'Tree File'
# Check parameters
test.print_variables()
# Submit the tree
print('')
print((
    'Uploading the tree.  This may take some time depending on how large the '
    'tree is and how much load there is on the itol server'
))
good_upload = test.upload()
if not good_upload:
    print('There was an error:' + test.comm.upload_output)
    sys.exit(1)

# Read the tree ID
print('Tree ID: ' + str(test.comm.tree_id))

# Read the iTOL API return statement
print('iTOL output: ' + str(test.comm.upload_output))

# Website to be redirected to iTOL tree
print('Tree Web Page URL: ' + test.get_webpage())

# Warnings associated with the upload
print('Warnings: ' + str(test.comm.warnings))


# Export a pre-made tree to pdf
#itol_exporter = ItolExport()
#itol_exporter.set_export_param_value('tree', '18793532031912684633930')
#itol_exporter.set_export_param_value('format', 'pdf')
#itol_exporter.set_export_param_value('datasetList', 'dataset1')
# itol_exporter.export('example_pdf.pdf')
# print('exported tree to ',export_location)

# Export the tree above to pdf
print('Exporting to pdf')
itol_exporter = test.get_itol_export()
export_location = os.path.join(current_dir, family_domain_ID + '_tree.pdf')
itol_exporter.set_export_param_value('format', 'pdf')
itol_exporter.set_export_param_value('datasetList', 'dataset1')
itol_exporter.export(export_location)
print('exported tree to ', export_location)
