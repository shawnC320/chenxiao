import json
import requests
from lxml import etree
from fake_useragent import UserAgent
from urllib.request import urlretrieve


class DoubanSpider(object):
    def __init__(self):
        self.baseurl = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&'
        self.headers = {
            "User-Agent" : UserAgent(verify_ssl=False).chrome
        }

    def getpages(self, params):
        response = requests.get(
            self.baseurl,
            params=params,
            headers=self.headers
        )
        response.encoding = 'utf-8'
        html = response.text
        self.save_data(html)

    def save_data(self, html):
        rDict = json.loads(html)
        result = rDict['subjects']
        #  "rate":"7.0",
        # "cover_x":7142,
        # "title":"飞驰人生",
        # "url":"https://movie.douban.com/subject/30163509/",
        # "playable":true,
        # "cover":"https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2542973862.jpg",
        # "id":"30163509",
        # "cover_y":10000,
        # "is_new":false
        for one_data in result:
            img_url = one_data['cover']
            img_name = one_data['id']
            with open('Spider/douban2.0/data/move.log', 'a') as f:
                for key in one_data:
                    f.write(str(one_data[key]))
                    f.write(' ')
                f.write('\r\n')
            print('保存基础电影数据成功')
            self.get_img(img_url, img_name)

    def get_img(self, url, name):
        res = requests.get(url, headers= self.headers)
        html = res.content
        with open('Spider/douban2.0/img/' + name + '.jpg', 'wb') as f:
            f.write(html)
            print('%s下载成功' % name)

    def main(self):
        begin = int(input('起始页：'))
        end = int(input('终止页：'))
        for i in range(begin, end):
            pn = i * 20
            params = {
                'page_start' : str(pn)
            }
            self.getpages(params)

if __name__ == "__main__":
    spider = DoubanSpider()
    spider.main()