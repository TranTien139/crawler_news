# -*- coding: utf-8 -*-

# Scrapy settings for craw_link_post project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'craw_link_post'

SPIDER_MODULES = ['craw_link_post.spiders']
NEWSPIDER_MODULE = 'craw_link_post.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'craw_link_post (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

CONFIG_XPATH = './config.cfg'

MYSQL_HOST = '127.0.0.1'
MYSQL_PORT = 3306
MYSQL_USER = 'tientv'
MYSQL_PASSWORD = '123789'
MYSQL_DB = 'crawler_news'
