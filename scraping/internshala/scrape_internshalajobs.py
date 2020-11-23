import requests
import json
import urllib.request
from bs4 import BeautifulSoup

class internshalajobs:

    def start(self,CURRENT_COUNT):

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
                except:jobs_images.append("")

        for i in range(len(jobs_company)):
            CURRENT_COUNT+=1
            jobs[CURRENT_COUNT] = {"company":jobs_company[i],
            "profile":jobs_profile[i],"link":jobs_link[i],"stipend":jobs_stipend[i],
            "img":jobs_images[i]}

        #self.write_json(jobs)
        return jobs

    def write_json(self,dictionary):
        with open("internshala.json", "w") as outfile:
            json.dump(dictionary, outfile, indent=4)

class intershala_internships:

    def start(self,count):
        internship_link = "https://internshala.com/internships/page-"

        profile = []
        company = []
        link = []
        img = []
        stipend = []

        internships = {}

        soups = []
        for i in range(1,207):
            r=requests.get(internship_link+str(i))
            soups.append(BeautifulSoup(r.content,'html5lib'))

        for soup in soups:
            for i in soup.find_all(class_="heading_4_5 profile"):
                profile.append(i.text.strip())

            for i in soup.find_all(class_="heading_6 company_name"):
                company.append(i.text.strip())

            for i in soup.find_all(class_="stipend"):
                stipend.append(i.text.strip())

            for i in soup.find_all(class_="view_detail_button"):
                link.append("https://internshala.com"+i['href'].strip())

            for i in soup.find_all(class_="internship_logo"):
                try:
                    img.append("https://internshala.com"+i.find('img')['src'].strip())
                except:img.append("")


        total_length = min([len(i) for i in [company,link,img,profile,stipend]])
        for i in range(total_length):
            count+=1
            internships[count]={"company":company[i],"profile":profile[i],"link":link[i],"stipend":stipend[i],"img":img[i]}

        self.write_json(internships)

        return internships

    def write_json(self,dicti):
        with open("internships.json", "w") as outfile:
            json.dump(dicti, outfile, indent=4)

obj=intershala_internships()
obj.start(10000520)