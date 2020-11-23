import os
import json

def check_duplicates(dictionary):
    duplicate_list = set()
    for i in dictionary:
        for j in dictionary:
            if j!=i:
                if dictionary[i]==dictionary[j]:
                    duplicate_list.add(i)

    for i in duplicate_list:
        del dictionary[i]

    return dictionary

json_list = []

for i in os.listdir("scraping"):
    for j in os.listdir('scraping/'+i):
        if ".json" in j:
            json_list.append("scraping/"+i+"/"+j)


final_data={}
for i in json_list:
    if "cybertecz" not in i.lower() and "lets intern" not in i.lower():
        try:
            with open(i) as json_file:
                data = json.load(json_file)
            final_data.update(data)
        except:print(i)

final_data = check_duplicates(final_data)

with open("final_data.json", "w") as outfile:
    json.dump(final_data, outfile, indent=4)