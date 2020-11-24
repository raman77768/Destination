import json
import scrapy
from scrapy.crawler import CrawlerProcess


class LetsInternScraper(scrapy.Spider):

    name = 'lets_intern_scraper'

    def start_requests(self):
        urls = ['pocket-money-internships','customer-service-internships','gurgaon-internships','delhi-internships','mumbai-internships','pune-internships','bangalore-internships','chennai-internships','hyderabad-internships','kolkata-internships','','it-internships','mba-internships','engineering-internships','marketing-internships','design-internships','journalism-internships','education-teaching-internships','content-media-internships','human-resources-internships','finance-internships','summer-internships','full-time-internships','online-virtual-internships','fresher-job-internships','part-time-internships','brand-ambassador-internships']
        for url in urls:
            yield scrapy.Request(url='https://www.letsintern.com/internships/'+url, callback=self.parse1)

    def parse1(self, response):
        links = response.css('div.job-apply-button>a::attr(href)').extract()
        for link in links:
            yield response.follow(url=link, callback=self.parse2)

    def parse2(self, response):
        global dick, id
        profile = response.css(
            'h4.truncate-normal.wrap-normal-mobile>a::text').extract_first()
        name = response.css('p.truncate-normal>a::text').extract_first()
        stipend = response.css('div#application-deadline>p::text').extract()
        img = response.css('div.company-logo-img::attr(style)').extract_first()
        temp = { 
            str(id): {
                'company': name,
                'profile': profile,
                'link': response.url,
                'stipend': ('Unpaid' if stipend[-1] == "Rs. 0" else stipend[-1]),
                'img': img.rstrip(" no-repeat scroll center;background-position:top right;height:100%;background-size:contain;").lstrip('background:url')[1:-1]
                }
            } 
        dick.update(temp) 
        id += 1
        


dick = {}
id = 20000427


process = CrawlerProcess()
process.crawl(LetsInternScraper)
process.start()


# print(dick)
print(id)


fout = open('letsintern.json', 'a')
json.dump(dick, fout, indent=6)
fout.close()