import json

f = open('posts.json',)

cru = json.load(f)

for i in cru['lol_data']:
    for j in i:
        print(i[j])
