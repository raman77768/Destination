import json
import scrapy
from scrapy.crawler import CrawlerProcess


class LetsInternScraper(scrapy.Spider):

    name = 'lets_intern_scraper'

    def start_requests(self):
        urls = ['https://www.letsintern.com/internships']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse1)

    def parse1(self, response):
        global links
        links = response.css('div.job-apply-button>a::attr(href)').extract()
        for link in links:
            yield response.follow(url=link, callback=self.parse2)

    def parse2(self, response):
        global dick, links, id
        name = response.css(
            'h4.truncate-normal.wrap-normal-mobile>a::text').extract()
        profile = response.css('p.truncate-normal>a::text').extract()
        stipend = response.css('div#application-deadline>p::text').extract()
        img = response.css('div.company-logo-img::attr(style)').extract()
        for i in range(len(name)):
            temp = {
                str(id): {
                    'company': name[i],
                    'profile': profile[i],
                    'link': 'https://www.letsintern.com/'+links[i],
                    'stipend': stipend[-1],
                    'img': img[i].rstrip(" no-repeat scroll center;background-position:top right;height:100%;background-size:contain;").lstrip('background:url')[1:-1]
                }
            }
            dick.update(temp)
            id += 1


dick, links = {}, []
id = 20000000


process = CrawlerProcess()
process.crawl(LetsInternScraper)
process.start()


print(dick)
print(id)


fout = open('letsintern.json', 'w')
json.dump(dick, fout, indent=6)
fout.close()
