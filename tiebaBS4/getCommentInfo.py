# -*- coding: utf-8 -*-
'''
Created on 2017.04.10

@Author : wujiu
'''

import urllib2
from bs4 import BeautifulSoup
from mylog import MyLog as mylog


class Item(object):
    title = None        # 帖子标题
    firstAuthor = None  # 帖子创建者
    firstTime = None    # 帖子创建时间
    reNum = None        # 总回复数
    content = None      # 最后回复内容
    lastAuthor = None   # 最后回复者
    lastTime = None     # 最后回复时间


class GetTiebaInfo(object):
    def __init__(self, url):
        self.url = url
        self.log = mylog()
        self.pageSum = 5
        self.urls = self.getUrls(self.pageSum)
        self.items = self.spider(self.urls)
        self.pipelines(self.items)

    def getUrls(self, pageSum):
        urls = []
