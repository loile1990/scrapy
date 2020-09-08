import scrapy
from scrapy import spiders
#from scrapy.spiders import BaseSpider
from scrapy.spiders import Spider
from scrapy.spiders import CrawlSpider

#from scrapy.selector import HtmlXPathSelector
from jobs.items import JobsItem

class MySpider(Spider):
    name = "job"
    allowed_domains = ["https://tuoitre.vn"]
    start_urls = ["https://tuoitre.vn/gia-vang-the-gioi-trong-nuoc-deu-lui-xu-huong-giam-sau-roi-tang-lai-20200908163059938.htm","https://tuoitre.vn/bo-nong-nghiep-yeu-cau-ra-soat-lai-toan-bo-ma-so-vung-trong-sau-vu-xoai-dong-thap-bi-mao-danh-20200907183933943.htm"]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        titles = hxs.xpath("//span[@class='article-title']  ")
        items = []
        for titles in titles:
            item = JobsItem()
            item["title"] = titles.select("a/text()").extract()
            #item["link"] = titles.select("a/@href").extract()
            items.append(item)
        return items