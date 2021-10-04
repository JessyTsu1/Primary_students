import scrapy

"""
# File: test.py
# Written by JessyTsui
# Time: 2021/10/4 00:40 上午
# IDE: PyCharm
# Have a good day！
"""

class TestSpider(scrapy.Spider):
    name = "test"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'
    }

    def start_requests(self):
        # urls = [
        #     'https://school.wjszx.com.cn/senior/introduce-14.html',
        #     'https://school.wjszx.com.cn/senior/introduce-15.html',
        # ]
        for i in range(1, 107438):
            url = "g".format(i)
        # for url in urls:
            yield scrapy.Request(url=url, callback=self.parse, headers=self.headers)

    def parse(self, response):
        
        name = '//h1/text()'
        Time = '/html/body/div[3]/div[2]/div/div[2]/div[1]/div[3]/ul/li[1]/@title'
        phone = '/html/body/div[3]/div[2]/div/div[2]/div[1]/div[3]/ul/li[2]/@title'
        address = '/html/body/div[3]/div[2]/div/div[2]/div[1]/div[3]/ul/li[3]/@title'
        url = '/html/body/div[3]/div[2]/div/div[2]/div[1]/div[3]/ul/li[4]/@title'
        name = response.xpath(name).get()
        Time = response.xpath(Time).get()
        phone = response.xpath(phone).get()
        address = response.xpath(address).get()
        url = response.xpath(url).get()

        page = response.url.split("/")[-1]
        filename = '%s.html' % page

        ## 把网页源代码保存下来
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log('Saved file %s' % filename)

        yield {
            'name': name,
            'Time': Time,
            'phone': phone,
            'address': address,
            'url': url,
        }