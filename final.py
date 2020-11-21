from scraping.scrape_internshalajobs import internshalajobs
import json

STARTING_COUNT = 10000000
END_COUNT = 19999999
CURRENT_COUNT = 10000000

def get_internshala_data(count):
    obj = internshalajobs()
    res = obj.start(count)

    return res

def merge_data(dict1, dict2):
    res = {**dict1, **dict2}
    return res

def write_json(final_dict):
    with open("final_data.json", "w") as outfile:
        json.dump(final_dict, outfile, indent=4)

if __name__ == "__main__":
    #pass
    final_data = get_internshala_data(CURRENT_COUNT)
    write_json(final_data)