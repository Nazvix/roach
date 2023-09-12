import scrapy

class BasicRoach(scrapy.Spider):
    name = "flying_trilobite"
    start_urls = ['http://quotes.toscrape.com']
    def parse(self, response):
        for quote in response.xpath('//div[@class="quote"]'):
            yield {
                'text': quote.xpath('span[@class="text"]/text()').extract_first(),
                'author': quote.xpath('span/small[@class="author"]/text()').extract_first(),
            }