import scrapy


class MacconstrutoraSpider(scrapy.Spider):
    name = "macconstrutora"
    allowed_domains = ["mac.com.br"]
    start_urls = ["https://mac.com.br/"]

    def parse(self, response):
        pass
