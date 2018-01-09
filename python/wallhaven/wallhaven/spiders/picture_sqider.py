import scrapy
from wallhaven.items import WallhavenItem


class PictureSpider(scrapy.Spider):
    name = "picture"

    def start_requests(self):
        baseurl = 'https://alpha.wallhaven.cc/toplist?page={page}'
        for page in range(1, 159):
            url = baseurl.format(page=page)
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for url_page in response.xpath('//div[@id="thumbs"]/section/ul/li/figure/a/@href').extract():
            yield scrapy.Request(url_page, callback=self.parse_picture)

    def parse_picture(self, response):
        source_url = response.xpath('//section[@id="showcase"]/div/img/@src').extract_first()
        item = WallhavenItem()
        item['image_urls'] = ['https:{0}'.format(source_url)]
        yield item
