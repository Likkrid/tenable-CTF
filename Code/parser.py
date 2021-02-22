#!/usr/bin/env python3

import re

def ParseNamesByGroup(blob, group_name):
    #impliment code
	regex_blob = re.findall('\[(.*?)]', blob)
	my_dicts = [ eval("{"+mydict+"}") for mydict in regex_blob]
	return [ i['user_name'] for i in my_dicts if i['Group'] == group_name]

#data = raw_input()
data = 'Black|+++,Bellhomes LLC.,["age":39, "user_name":"Reid Jolley", "Group":"Black"],+++,Greek Ideas,["age":63, "user_name":"Lucius Chadwell", "Group":"Green"],["age":63, "user_name":"Cary Rizzuto", "Group":"Black"],["age":28, "user_name":"Shoshana Bickett", "Group":"Yellow"],["age":69, "user_name":"Madeleine Swallow", "Group":"Green"],["age":41, "user_name":"Buddy Etter", "Group":"Black"],+++,God fire,["age":26, "user_name":"Carlene Caulder", "Group":"Green"],["age":43, "user_name":"Napoleon Peay", "Group":"Purple"],["age":44, "user_name":"Noemi Constant", "Group":"Green"]'

group_name = data.split('|')[0]
blob = data.split('|')[1]
result_names_list = ParseNamesByGroup(blob, group_name)
print (result_names_list)