##Given a list of specific gene GO ids, use quickGO api to find their more broad GO terms
import requests, sys
from collections import defaultdict
import json

#Get children GO IDs for Biological Processes category ie second tier GO terms (can be changed to any of the three broad GO terms given the specific GO ID)
requestURL = "https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0008150/children" #Number following GO%3A is GO ID associated with biological processes

r = requests.get(requestURL, headers={ "Accept" : "application/json"})

if not r.ok:
  r.raise_for_status()
  sys.exit()

responseBody = r.text

second_tier_GOterms = []
res_split = responseBody.split('"children":')
for item in res_split:
    if item.startswith('[{"id'):
        IDs = item.split('"id":')
        for term in IDs:
            if term.startswith('"GO'):
                GO_ID = term.split(',')[0].strip('"')
                second_tier_GOterms.append(GO_ID)


BP_childrenGOs = defaultdict(list)
for GO in second_tier_GOterms:
    BP_childrenGOs["GO:0008150"].append(GO)


#For each BP children GO ID, get their children GO IDs ie third tier GO terms - create dictionary of parent to children IDs
thirdT_GOids = []
BP_secondTier_thirdTier = defaultdict(list)
for GO in second_tier_GOterms:
    GOID = GO[3:]
    requestURL = "https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A" + GOID + "/children"

    r = requests.get(requestURL, headers={ "Accept" : "application/json"})

    if not r.ok:
        r.raise_for_status()
        sys.exit()

    responseBody_third = r.text

    third_tier_GOterms = []
    res_split_third = responseBody_third.split('"children":')
    for item in res_split_third:
        if item.startswith('[{"id'):
            IDs = item.split('"id":')
            for term in IDs:
                if term.startswith('"GO'):
                    GO_ID = term.split(',')[0].strip('"')
                    third_tier_GOterms.append(GO_ID)
                    thirdT_GOids.append(GO_ID)

    for child_GO in third_tier_GOterms:
        BP_secondTier_thirdTier[GO].append(child_GO)



############################################################################################### 


#Now that we have dictionary of specific GO terms to broad GO terms, use this to find broad GO terms for your user defined list of specific GO IDs



#Open dictionary of comp fams to specific GO IDs
with open('BP_results/compFams_BP_GOIDs.json') as f:
  fam_GOids = json.load(f)

#Get full list of GO terms in the dictionary
GO_list = []
for k, v in fam_GOids.items():
  for GOid in v:
    GO_id = 'GO:' + GOid
    GO_list.append(GO_id)


GO_list = set(GO_list)

#For each specific GO ID, create a dictionary of it to its broader GO ID
specGO_broadGO = defaultdict(list)

for GO in GO_list:
  GOID = GO[3:]
  requestURL = "https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A" + GOID + "/ancestors?relations=is_a"

  r = requests.get(requestURL, headers={ "Accept" : "application/json"})
  
  if not r.ok:
    r.raise_for_status()
    sys.exit()

  responseBody = r.text

  ancestor_list = []
  res_split = responseBody.split('"ancestors":') #Split output file to get ancestor GO IDs
  for item in res_split:
    if item.startswith('["GO'):
      terms = item.split('],')
      GO_terms = terms[0]
      for GOs in GO_terms.split(','):
        GOIDs = GOs.strip('[').strip('"')
        ancestor_list.append(GOIDs) #Create list of the ancestor GO IDs

  #If the ancestor GO id is in the third tier GO list, use this GO ID as functional annotation for the gene
  for ancesID in ancestor_list:
    if ancesID in thirdT_GOids:
      specGO_broadGO[GO].append(ancesID)
    #If the ancestor GO id is in the second tier GO ids continue
    elif ancesID in second_tier_GOterms:
      continue
    #If the GO id is itself in the third tier GO ids, use this ID
    else:
      if GO in thirdT_GOids:
        specGO_broadGO[GO].append(GO)


#Save your specific to broad GO ids to a dictionary for later parsing
with open('specGO_2_broadGO_BP.json', 'w') as outD:
  json.dump(specGO_broadGO, outD)

#Get function names of GO terms in specific to broad GO terms
#all_GO_list = []
#for k, v in specGO_broadGO.items():
#  all_GO_list.append(k)
  
#  print(k, set(v), len(set(v)))


