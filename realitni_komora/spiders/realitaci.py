# -*- coding: utf-8 -*-
import scrapy
import re

from realitni_komora.items import RealitniKomoraItem


class RealitniKomoraSpider(scrapy.Spider):
    name = 'realitni_komora'
    allowed_domains = ['realitnikomora.cz']
    start_urls = [
        'https://www.realitnikomora.cz/komora.php?sekce=list_items']

    custom_settings = {
        'FEED_EXPORT_ENCODING': 'utf-8'
    }

    def parse_realitak(self, response):
        try:
            telefon = response.xpath(
                "//td['@class=padding5 td_line']/span[text()[contains(., 'Telefon')]]/following-sibling::span/text()").extract_first()
            id = response.xpath(
                "//td['@class=padding5 td_line']/span[text()[contains(., 'Členské ID')]]/following-sibling::span/text()").extract_first()
            jmeno = response.xpath(
                "//td['@class=padding5 td_line']/span[text()[contains(., 'Jméno')]]/following-sibling::span/span/text()").extract_first()
            realitkaUrl = response.xpath(
                "//td['@class=padding5 td_line']/span[text()[contains(., 'Realitní kancelář')]]/following-sibling::span/a/@href").extract_first()
            realitkaMeno = response.xpath(
                "//td['@class=padding5 td_line']/span[text()[contains(., 'Realitní kancelář')]]/following-sibling::span/a/b/span/text()").extract_first()
            mail = response.xpath(
                "//td['@class=padding5 td_line']/span[text()[contains(., 'E-mail')]]/following-sibling::span/a/b/text()").extract_first()
            ic = response.xpath(
                "//td['@class=padding5 td_line']/span[text()[contains(., 'IČ')]]/following-sibling::span/text()").extract_first()

            item = RealitniKomoraItem()
            item['id'] = id
            item['jmeno'] = jmeno
            item['telefon'] = telefon
            item['mail'] = mail
            item['realitkaUrl'] = realitkaUrl
            item['realitkaMeno'] = realitkaMeno
            item['ic'] = ic
            item['url'] = response.url

            yield item

        except Exception as e:
            print(e)

    def parse_page(self, response):
        try:
            makleri = response.xpath(
                '//table["@class=dotsTable"]//tbody//tr//td//a/@href').extract()
            makleriSet = set(makleri)
            for makler in makleriSet:
                url = "https://www.realitnikomora.cz" + str(makler)
                yield scrapy.Request(url=url, callback=self.parse_realitak)

        except Exception as e:
            print(e)

    def parse(self, response):
        try:
            paggination = response.xpath(
                '//div[@class="paging"]/a/@href').extract()
            lastNum = str(paggination[-2]).split("=")[-1]
            for i in range(30, int(lastNum) + 30, 30):
                url = "http://www.realitnikomora.cz/komora.php?sekce=list_items&lim1=" + \
                    str(i)
                yield scrapy.Request(url=url, callback=self.parse_page)

        except Exception as e:
            print(e)
