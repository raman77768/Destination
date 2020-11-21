import os
import json

json_list = []

for i in os.listdir("scraping"):
    for j in os.listdir('scraping/'+i):
        if ".json" in j:
            json_list.append("scraping/"+i+"/"+j)


final_data={}
for i in json_list:
    if "cybertecz" not in i.lower():
        with open(i) as json_file:
            data = json.load(json_file)
        final_data.update(data)


with open("final_data.json", "w") as outfile:
    json.dump(final_data, outfile, indent=4)