from scrape_internshalajobs import internshalajobs

STARTING_COUNT = 10000000
END_COUNT = 19999999
CURRENT_COUNT = 10000000

def get_internshala_data(count):
    internshalajobs(count)

if __name__ == "__main__":
    get_internshala_data(CURRENT_COUNT)