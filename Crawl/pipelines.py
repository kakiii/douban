# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os

class CrawlPipeline(object):
    def process_item(self, item, spider):
        item["title"]="".join(item["title"])
        item["href"]="".join(item["href"])
        item["status"]="".join(item["status"])
        item["ranking"]="".join(item["ranking"])
        item["description"]="".join(item["description"])
        item["quote"]="".join(item["quote"])
        with open('Top_250_movie.txt', 'a', encoding='utf-8') as f:
            f.write(str(rank)+';'+str(name)+';'+str(ranking)+';'+str(href)+';'+str(description)+';'+str(quote)+'\n')
            f.close()
        return item

