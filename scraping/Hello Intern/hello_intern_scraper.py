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
        links = response.css('span.title_span>a::attr(href)').extract()
        for link in links:
            yield response.follow(url='https://www.hellointern.com'+link, callback=self.parse2)

    def parse2(self, response):
        global dick, id
        stipend = response.css('span.ip_cont_dp::text').extract()
        img = response.css('td.dptd>img::attr(src)').extract_first()
        temp = {
            str(id): {
                'company': stipend[1],
                'profile': stipend[0],
                'link': response.url,
                'stipend': stipend[7],
                'img': 'https://www.hellointern.com'+str(img)
            }
        }
        dick.update(temp)
        id += 1


dick = {}
id = 20000853


process = CrawlerProcess()
process.crawl(HelloInternScraper)
process.start()


# print(dick)
print(id)


fout = open('hellointern.json', 'w')
json.dump(dick, fout, indent=4)
fout.close()
