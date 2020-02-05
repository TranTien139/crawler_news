# !/usr/bin/env python
# _*_ coding: utf-8 _*_


import scrapy
import configparser
from scrapy.conf import settings
# from craw_link_post.common.database import Database

class ArticleCrawler(scrapy.Spider):
	name ="news"
	
	def __init__(self):
		pass
		# con = Database()._connect_db()
		# self.conn = con["conn"]
		# self.cursor = con["cursor"]
	
	def get_config(self, link=''):
		parse_link = configparser.ConfigParser()
		parse_link.read(settings.get('CONFIG_XPATH'), encoding="utf8")
		domain = link.split("://")[-1].split('/')[0].split('?')[0]
		out = dict()
		out['path'] = parse_link.get(domain, 'path')
		out['domain'] = link.split("://")[0] + "://" + domain
		return out
	
	def start_requests(self):
		urls = [
			"https://kr.investing.com/crypto/bitcoin/news"
		]
		for url in urls:
			yield scrapy.Request(url=url, callback=self.parse)
	
	def parse(self, response):
		xpath = self.get_config(response.url)
		links = response.selector.xpath(xpath["path"]).extract()
		for link in links:
			if link and (xpath["domain"] not in link):
				if '/' in link:
					link = xpath["domain"] + link
				else:
					link = xpath["domain"] + '/' + link
			item = {}
			item['url'] = link
			item['domain'] = xpath["domain"]
			# Database()._insert_post(self.conn, self.cursor, item)
			print(link, "url")