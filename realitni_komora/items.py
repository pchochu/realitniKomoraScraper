# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class RealitniKomoraItem(scrapy.Item):
    id = scrapy.Field()
    jmeno = scrapy.Field()
    telefon = scrapy.Field()
    mail = scrapy.Field()
    realitkaUrl = scrapy.Field()
    realitkaMeno = scrapy.Field()
    ic = scrapy.Field()
    url = scrapy.Field()
