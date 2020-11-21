import json
import scrapy
from scrapy.crawler import  CrawlerProcess


class JobquestScraper(scrapy.Spider):
    
    name='jobquest_scraper'
    
    def start_requests(self):
        urls = ['https://jobsquest.co/listings/']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse1) 
       
            
    def parse1(self,response):
        name=response.css('h3.card-title::text').extract()
        print(name)
            
    # def parse2(self,response):
    #     name=response.css('p:nth-of-type(2) ::text').extract()
    #     profile=response.css('p:nth-of-type(5)>strong ::text').extract()
    #     stipend=response.css('p:nth-of-type(8) ::text').extract()
    #     for i in range(len(name)):
    #         temp={
    #             name[i]:{
    #                 'profile':(profile[i].split(':')[-1]).strip(),
    #                 'link':links[i],
    #                 'stipend':(stipend[i] if 'salary' in stipend[i].split(':') else 'NA') 
    #             }
    #         }
    #         dick.update(temp)
       
dick,links={},[]     

process=CrawlerProcess()
process.crawl(JobquestScraper)
process.start()        

# fout=open('cybertecz.json','a')
# json.dump(dick,fout,indent=6)
# fout.close()