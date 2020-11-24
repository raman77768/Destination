import os
import json
<<<<<<< HEAD
<<<<<<< HEAD
from rating_data.fetch_data import rating

json_list = []
Rating_obj = rating()
=======
>>>>>>> Add files via upload
=======
>>>>>>> 2ba2ef134a87969f279a250724230f31072f8c42

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

<<<<<<< HEAD
<<<<<<< HEAD
def getrating(company_name):
    rating = Rating_obj.get_rating(company_name)
    return rating

=======
json_list = []
>>>>>>> Add files via upload
=======
json_list = []
>>>>>>> 2ba2ef134a87969f279a250724230f31072f8c42

for i in os.listdir("scraping"):
    for j in os.listdir('scraping/'+i):
        if ".json" in j:
            json_list.append("scraping/"+i+"/"+j)


final_data={}
for i in json_list:
<<<<<<< HEAD
<<<<<<< HEAD
    if "cybertecz" not in i.lower():
=======
    if "cybertecz" not in i.lower() and "lets intern" not in i.lower():
>>>>>>> Add files via upload
=======
    if "cybertecz" not in i.lower() and "lets intern" not in i.lower():
>>>>>>> 2ba2ef134a87969f279a250724230f31072f8c42
        try:
            with open(i) as json_file:
                data = json.load(json_file)
            final_data.update(data)
<<<<<<< HEAD
<<<<<<< HEAD
        except:pass

final_data = check_duplicates(final_data)
for i in final_data:
    final_data[i]['rating'] = getrating(final_data[i]['company'])

=======
        except:print(i)

final_data = check_duplicates(final_data)
>>>>>>> Add files via upload
=======
        except:print(i)

final_data = check_duplicates(final_data)
>>>>>>> 2ba2ef134a87969f279a250724230f31072f8c42

with open("final_data.json", "w") as outfile:
    json.dump(final_data, outfile, indent=4)