import scrapy


class MacspiderSpider(scrapy.Spider):
    name = "macspider"
    allowed_domains = ["mac.com.br"]
    start_urls = ["https://mac.com.br/empreendimentos"]

    def parse(self, response):
        pass
