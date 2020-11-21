import requests
import json
import urllib.request
from bs4 import BeautifulSoup

class internshalajobs:

    def __init__(self,CURRENT_COUNT):

        internshala_link = "https://internshala.com/fresher-jobs/page-"

        soups = []
        for i in range(1,14):
            r = requests.get(internshala_link+str(i))
            soups.append(BeautifulSoup(r.content, 'html5lib'))

        jobs_profile = []
        jobs_company = []
        jobs_link = []
        jobs_stipend = []
        jobs_images = []

        jobs = {}

        for soup in soups:
            for i in soup.find_all(class_="heading_4_5 profile"):
                jobs_profile.append(i.text.strip())

            for i in soup.find_all(class_="heading_6 company_name"):
                jobs_company.append(i.text.strip())

            for i in soup.find_all("a",class_="view_detail_button"):
                jobs_link.append("https://internshala.com"+i['href'].strip())

            s = soup.find_all(class_="item_body")
            for i in range(1,len(s),3):
                jobs_stipend.append(s[i].text.strip())
            for i in soup.find_all(class_="internship_logo"):
                try:
                    jobs_images.append("https://internshala.com"+i.find('img')['src'].strip())
                except:jobs_images.append("https://drive.google.com/file/d/1nkVjVqNr5qP4f0NqMGgt_lBgrfdPPOyQ/view?usp=sharing")

        for i in range(len(jobs_company)):
            CURRENT_COUNT+=1
            jobs[CURRENT_COUNT] = {"company":jobs_company[i],
            "profile":jobs_profile[i],"link":jobs_link[i],"stipend":jobs_stipend[i],
            "img":jobs_images[i]}


        self.write_json(jobs)


    def write_json(self,dictionary):
        with open("internshala.json", "w") as outfile:
            json.dump(dictionary, outfile, indent=4)
