import scrapy


class JiomartSpider(scrapy.Spider):
    name = "jiomart"
    allowed_domains = ["www.jiomart.com"]
    start_urls = ["https://www.jiomart.com"]

    def parse(self, response):
        pass
