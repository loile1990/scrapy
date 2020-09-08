# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import spider
from scrapy.spider import BaseSpider
from scrapy.spiders import CrawlSpider
from scrapy.spiders import Spider
from scrapy.selector import HtmlXPathSelector
from jobs.items import JobsItem


class JobsItem(scrapy.Item):
    # define the fields for your item here like:
	title = scrapy.Field()
    name = scrapy.Field()
    pass
