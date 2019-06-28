import json


with open('json_dict.json', 'r') as jsdict:
    js_dictlist = json.load(jsdict)
for i in js_dictlist.keys():
    list_dict = js_dictlist[i]
line_keys = []
line_value = []
for i in list_dict:
    if isinstance(i, dict) is True:
        for i_key in i.keys():
            line_keys.append(i_key)
        for l_key in i.values():
            line_value.append(l_key)
with open('7_1.csv', 'w') as csv_file:
    for i in range(len(line_keys)):
        csv_file.write(line_keys[i]+','+str(line_value[i])+'\n')
