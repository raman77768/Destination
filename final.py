import os
import json
from rating_data.fetch_data import rating

json_list = []
Rating_obj = rating()

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

def getrating(company_name):
    rating = Rating_obj.get_rating(company_name)
    return rating


for i in os.listdir("scraping"):
    for j in os.listdir('scraping/'+i):
        if ".json" in j:
            json_list.append("scraping/"+i+"/"+j)


final_data={}
for i in json_list:
    if "cybertecz" not in i.lower():
        try:
            with open(i) as json_file:
                data = json.load(json_file)
            final_data.update(data)
        except:pass

final_data = check_duplicates(final_data)
for i in final_data:
    final_data[i]['rating'] = getrating(final_data[i]['company'])


with open("final_data.json", "w") as outfile:
    json.dump(final_data, outfile, indent=4)