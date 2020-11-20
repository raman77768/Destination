import json
import scrapy
from scrapy.crawler import  CrawlerProcess


class InternshipScraper(scrapy.Spider):
    
    name='internship_scraper'
    
    def start_requests(self):
        urls = ['https://jobs.cybertecz.in/category/freshers/']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse1) 
       
            
    def parse1(self,response):
        global links
        links_upper=response.css('div.td-module.thumb>a::attr(href)').extract()
        links_lower=response.css('h3.entry-title.td-module-title>a::attr(href)').extract()
        links=links_lower+links_upper
        for link in links:
            yield response.follow(url=link, callback=self.parse2)
            
    def parse2(self,response):
        global links,dick
        name=response.css('p:nth-of-type(2) ::text').extract()
        profile=response.css('p:nth-of-type(5)>strong ::text').extract()
        stipend=response.css('p:nth-of-type(8) ::text').extract()
        for i in range(len(name)):
            temp={
                name[i]:{
                    'profile':(profile[i].split(':')[-1]).strip(),
                    'link':links[i],
                    'stipend':(stipend[i] if 'salary' in stipend[i].split(':') else 'NA') 
                }
            }
            dick.update(temp)
       
dick,links={},[]     

process=CrawlerProcess()
process.crawl(InternshipScraper)
process.start()        

fout=open('cybertecz.json','w+')
json.dump(dick,fout,indent=6)
fout.close()