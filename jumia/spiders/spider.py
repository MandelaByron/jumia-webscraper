import scrapy
from ..items import JumiaItem

class SpiderSpider(scrapy.Spider):
    name = "spider"
    allowed_domains = ["jumia.co.ke"]
    start_urls = ["https://www.jumia.co.ke/mlp-top-deals/"]

    custom_settings = {
        'FEEDS':{
            'products_data.json':{
                'format':'json',
                'overwrite':True
            },
            
        },
        
        'LOG_FILE':'logs.txt',
        'LOG_LEVEL':'INFO',
        'LOG_FILE_APPEND':False
    }
    def parse(self, response):
        
        items = JumiaItem()
        products = response.xpath('//article[@class="prd _fb _p col c-prd"]')
        
        for product in products:
            name = product.xpath('.//h3[@class="name"]/text()').get()
            
            link = response.urljoin(product.xpath('.//a[@class="core"]').attrib['href']) 
            
            price = product.xpath('.//div[@class="prc"]/text()').get()
            
            review = product.xpath('.//div[@class="stars _s"]/text()').get()
            
            items['product_name'] = name
            
            items['link'] = link
            
            items['price'] = price
            
            items['review'] = review

            
            yield items
            
        next_page = response.xpath('//a[@aria-label="Next Page"]/@href').get()
        
        if next_page:
            next_page_url = response.urljoin(next_page)
            yield scrapy.Request(next_page_url, callback=self.parse)
