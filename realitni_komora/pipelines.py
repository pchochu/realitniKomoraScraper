# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exporters import JsonLinesItemExporter


class RealitaciPipeline(object):
    def process_item(self, item, spider):
        return item


class JsonExportPipeline(object):

    def __init__(self):
        self.file_name = 'realitaci.json'
        self.file_handle = None

    def open_spider(self, spider):
        print('JsonExportPipeline Exporter opened')

        file = open(self.file_name, 'wb')
        self.file_handle = file

        self.exporter = JsonLinesItemExporter(
            file, encoding='utf-8', ensure_ascii=False)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        print('JsonExportPipeline Exporter closed')
        self.exporter.finish_exporting()
        self.file_handle.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item
