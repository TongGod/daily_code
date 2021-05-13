import json

local_file = './test.json'
contrast_file = './contrast.json'

with open(local_file, 'r') as f:
    local = f.read()
    dict_local = json.loads(local)

with open(contrast_file, 'r') as f:
    contrast = f.read()
    dict_contrast = json.loads(contrast)

local_data = dict_local['allData'][0]['regressionData']
contrast_data = dict_contrast['allData'][0]['regressionData']

for i in range(0, len(local_data)):
    keys = list(local_data[i].keys())
    for j in keys:
        if str(local_data[i][j]) != str(contrast_data[i][j]):
            print({j: contrast_data[i][j]})

