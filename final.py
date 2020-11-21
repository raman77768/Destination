import os
import json

json_list = []

for i in os.listdir("scraping"):
    for j in os.listdir('scraping/'+i):
        if ".json" in j:
            json_list.append("scraping/"+i+"/"+j)

print(json_list)
for i in json_list:
    f1data = f2data = ""
    with open('final_data.json') as f1:
        f1data = f1.read()
    with open(i) as f2:
        f2data = f2.read()

    f1data += "\n"
    f1data += f2data
    with open ('final_data.json', 'a') as f3:
        f3.write(f1data)