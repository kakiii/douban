#coding: utf-8
import scrapy
from Crawl.items import DoubanItem
from scrapy.crawler import CrawlerProcess

class DoubanSpider(scrapy.Spider):
   name = "douban"
   allowed_domains = ["movie.douban.com"]
   start_urls = [
      "https://movie.douban.com/top250"
   ]

   def parse(self, response):
      blist = response.css(".all-img-list li")
      result = []
      if blist is None:
         print(u"\n\n\n\n****************** 消息提醒 ****************\n\n 未获取到电影列表！\n\n")
         yield scrapy.Request(start_urls[0],callback=self.parse)
      else:
         print(u"\n\n\n\n****************** 抓取到列表 ****************\n\n")
      for index in response.css('div.item'):
         
         item = DoubanItem()

         tmp = index.css("div.info div.hd a span.title::text").extract_first()
         item["title"] = tmp 
         item["href"] = index.css("div.pic a::attr(href)").extract()


         item["ranking"] = index.css("div.info div.bd div.star span.rating_num::text").extract()
         item["status"] = index.css("div.info div.hd  span.playable::text").extract()
         item["quote"] = index.css("div.info div.bd p.quote span.inq::text").extract_first() 
         item["description"] = index.css("div.info div.bd p::text").extract()
         print(u'%s【%s】 ==> %s' % (item["title"], item["description"], item["href"]))

         if item["href"] is not None:
            print(u"访问详情页：%s" % item["href"])
            yield scrapy.Request(str(item["href"]),callback=self.parse_detail,meta={"item": item})
         else:
            print(u"\n\n******************* 完成 *********************\n\n")

      next_url = response.css("span.next a::attr(href)").extract()
      if next_url:
        next_url = 'https://movie.douban.com/top250' + next_url[0]
        yield scrapy.Request(next_url, callback=self.parse, dont_filter=True)

   def parse_detail(self,response):
      item = response.meta["item"]
      #item["desc"] = "\n".join(response.css(".book-intro *::text").extract())
      #tmp = response.css(".book-state li")[0]
      #item["tag"] = ",".join(tmp.css(".tag-wrap a::text").extract())
      #item["recommend"] = ",".join(response.css(".like-more-list li h4 a::text").extract())
      print(u"*** 【%s】 ***" % item["title"])
      print(u"*** 描述：%s" % item["description"])
      print(u"*** 评分：%s" % item["ranking"])
      print(u"*** 状态：%s" % item["status"])
      # print(u"*** 梗概：%s" % item["desc"])
      print(u"*** 引言：%s" % item["quote"])
      print("*****************\n")
      yield item

      document.querySelector("#content > div > div.article > div.paginator > span.next > a")