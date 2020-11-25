import json
import scrapy
from scrapy.crawler import CrawlerProcess


class HelloInternScraper(scrapy.Spider):

    name = 'hello_intern_scraper'

    def start_requests(self):
        urls = ['https://www.hellointern.com/search']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse1)

    def parse1(self, response):
        global profile,name,stipend
        links = response.css('span.title_span>a::attr(href)').extract()
        profile = response.css('span.title_span>a::text').extract()
        name = response.css('span.name_span>a::text').extract()
        stipend = response.css('span.salary_span::text').extract()
        for link in links:
            yield response.follow(url='https://www.hellointern.com'+link, callback=self.parse2)

    def parse2(self, response):
        global dick,id,name,stipend,profile
        img = response.css('td.dptd>img::attr(src)').extract_first()
        for i in range(len(name)):
            temp={
                str(id):{
                    'company':name[i],
                    'profile':profile[i],
                    'link':response.url,
                    'stipend':stipend[i*2],
                    'img':'https://www.hellointern.com'+str(img)
                }
            }
            dick.update(temp)
            id+=1


dick,name,profile,stipend = {},[],[],[]
id= 20176827


process = CrawlerProcess()
process.crawl(HelloInternScraper)
process.start()


#print(dick)
print(id)


fout = open('hellointern.json', 'w')
json.dump(dick, fout, indent=4)
fout.close()
