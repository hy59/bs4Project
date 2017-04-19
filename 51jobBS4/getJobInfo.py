# -*- coding: utf-8 -*-

import urllib2
from bs4 import BeautifulSoup
from mylog import MyLog as mylog


class PythonJobItem(object):
    name = None          # 职位名称
    company = None       # 公司名称
    city = None          # 工作地点
    salary = None        # 薪资


class GetPythonJobInfo(object):

    def __init__(self):
        self.urls = []
        self.log = mylog()
        self.getUrls()
        self.items = self.spider(self.urls)
        self.pipelines(self.items)

    def getUrls(self):
        URL = r'http://search.51job.com/jobsearch/search_result.php?fromJs=1&jobarea=000000%2C00&district=000000&funtype=0000&industrytype=00&issuedate=9&providesalary=99&keyword=python&keywordtype=2&curr_page=2&lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&list_type=0&fromType=14&dibiaoid=0&confirmdate=9'
        htmlContent = self.getResponseContent(URL)
        soup = BeautifulSoup(htmlContent, 'lxml')
        tag = soup.find('div', attrs={'class': 'p_in'})
        pages = tag.a.get_text()
        for i in xrange(1, 10):
            url = r'http://search.51job.com/list/000000,000000,0000,00,9,99,python,2,'+str(i)+'.html'
            self.urls.append(url)
            self.log.info(u'添加URL：%s 到 URLS \r\n' %url)

    def getResponseContent(self, url):
        try:
            response = urllib2.urlopen(url.encode('utf8'))
        except:
            self.log.error(u'Python 返回URL：%s 数据失败 \r\n' %url)
        else:
            self.log.info(u'Pyhton 返回URL： %s 数据成功 \r\n' %url)
            return response.read()

    def spider(self, urls):
        items = []
        for url in urls:
            htmlContent = self.getResponseContent(url)
            soup = BeautifulSoup(htmlContent, 'lxml')
            tags = soup.find_all('div', attrs={'class': 'el'})

            for tag in tags:
                item = PythonJobItem()

                item.name = tag.find('p', attrs={'class': 't1'}).get_text().strip()
                item.company = tag.find('span', attrs={'class': 't2'}).get_text().strip()
                item.city = tag.find('span', attrs={'class': 't3'}).get_text().strip()
                item.salary = tag.find('span', attrs={'class': 't4'}).get_text().strip()
                items.append(item)
                self.log.info(u'获取工作为：%s 的数据成功' %(item.name))
        return items

    def pipelines(self, items):
        fileName = u'Python招聘.txt'.encode('GBK')
        with open(fileName, 'w') as fp:
            for item in items:
                fp.write('name:%s \t company:%s \t city:%s \t salary:%s \n'
                        %(item.name.encode('utf8'), item.company.encode('utf8'),
                          item.city.encode('utf8'), item.salary.encode('utf8')))
                self.log.info(u'将职位为: %s 的数据存入"%s"...' %(item.name, fileName.decode('GBK')))


if __name__ == '__main__':
    GPJI = GetPythonJobInfo()
