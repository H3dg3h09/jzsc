# -*- coding: utf-8 -*-
from scrapy_redis.spiders import RedisSpider
import redis
from jzsc.settings import REDIS_URL
import logging
from scrapy import FormRequest
import time


class GetidSpider(RedisSpider):
    name = 'getid'
    redis_key = 'getidspider:start_urls'
    _rds = redis.from_url(REDIS_URL, db=0, decode_responses=True)
    custom_settings = {
        'LOG_FILE': 'jzsc\log\{name}_{t}.txt'.format(name=name, t=time.strftime('%Y-%m-%d', time.localtime()))
    }
    form_data = {
        '$reload': '0',
        '$pgsz': '15',
    }
    page = 1
    cookie = {}
    max_page = 0
    def parse(self, response):
        hrefs = response.xpath('//tbody[@class="cursorDefault"]/tr/td/a/@href').extract()

        for href in hrefs:
            new_url = response.urljoin(href)
            self._rds.rpush('baseinfospider:start_urls', new_url)

            logging.log(logging.INFO, "{url}".format(url=new_url))


            if not self.max_page:
                import re
                self.max_page = int(re.search(r'pc:\d(.*?),', response.xpath('//a[@sf="pagebar"]').extract_first()).group(1))
                self.form_data['$total'] = re.search(r'tt:\d(.*?),', response.xpath('//a[@sf="pagebar"]').extract_first()).group(1)
                self.cookies = eval(response.headers.get('cookies', {}))


            self.page += 1
            if self.page <= self.max_page:
                self.form_data['$pg'] = str(self.page)

                yield FormRequest(response.url, callback=self.parse,
                                  cookies=self.cookies,
                                  formdata=self.form_data, dont_filter=True)


