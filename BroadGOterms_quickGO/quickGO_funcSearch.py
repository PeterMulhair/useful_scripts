#Given a the dictionary of specific to broad GO IDs, create a dictionary of the broad GO IDs to the functional GO term
import requests, sys
import json


with open('specGO_2_broadGO_BP.json') as f:
  GO_dict = json.load(f)


#Create a list of the broad GO IDs in the dictionary
broadGO_2_func = dict()
ID_list = []
for k, v in GO_dict.items():
  for ID in v:
    ID_list.append(ID)

ID_list = set(ID_list)

#Use the QuickGO API to get the actual function of each of the broad GO IDs
for ID in ID_list:
  GO_ID = ID[3:]
  requestURL = "https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=GO%3A" + GO_ID + "&limit=1&page=1"
  r = requests.get(requestURL, headers={ "Accept" : "application/json"})
  if not r.ok:
    r.raise_for_status()
    sys.exit()

  responseBody = r.text
  res_split = responseBody.split('"name":')
  for item in res_split:
    if item.startswith('"'):
      IDs = item.split('","')
      func = IDs[0].strip('"')

      broadGO_2_func[ID] = func

#Create a dictionary of broad GO IDs to their function
with open('broadGO_functions_BP.json', 'w') as outD:
  json.dump(broadGO_2_func, outD)

