# -*- coding: utf-8 -*-
from scrapy_redis.spiders import RedisSpider
from ..items import BasicInfoItem, CredentialsItem,\
                    PersonItem, ProgressItem
from scrapy import Request
import time


class BaseinfoSpider(RedisSpider):
    name = 'baseinfo'
    redis_key = 'baseinfospider:start_urls'
    custom_settings = {
        'LOG_FILE': 'jzsc\log\{name}_{t}.txt'.format(name=name, t=time.strftime('%Y-%m-%d', time.localtime()))
    }

    def parse(self, response):
        base_div = response.xpath('//div[@class="user_info spmtop"]')[0]
        name = base_div.xpath('b/text()').extract_first()
        info = base_div.xpath('following-sibling::table[1]/tbody/tr/td/text()').extract()

        base_item = BasicInfoItem()
        base_item['table_name'] = 'jz_info'
        base_item['name'] = name
        base_item['social_code'] = info[0]
        base_item['legal_re'] = info[1]
        base_item['com_type'] = info[2]
        base_item['province'] = info[3]
        base_item['addr'] = info[4]
        yield base_item

        urls_ = response.xpath('//ul[@class="tinyTab datas_tabs"]/li/a/@data-url').extract()
        urls = {
            'credential_url_': urls_[0],
            'person_url_': urls_[1],
            'progress_url_': urls_[2],
            'g_behavior_url_': urls_[3],
            'b_behavior_url_': urls_[4],
            'blacklist_url_': urls_[5],
        }

        credential_url_ = urls_[0]
        credential_url = response.urljoin(credential_url_)

        cookies = eval(response.headers['cookies'])
        yield Request(credential_url, callback=self.get_credential,
                      meta={'social_code': info[0], 'urls': urls, 'cookies':cookies},
                      cookies=cookies, dont_filter=True)

    def get_credential(self, response):
        trs = response.xpath('//table[@id="catabled"]/tbody/tr')
        for tr in trs:
            tds = tr.xpath('td')
            c_item = CredentialsItem()
            c_item['table_name'] = 'jz_credentials'
            c_item['social_code'] = response.meta['social_code']

            c_item['c_type'] = tds[1].xpath('string(.)').extract_first()
            c_item['c_code'] = tds[2].xpath('string(.)').extract_first()
            c_item['c_name'] = tds[3].xpath('string(.)').extract_first().strip()
            c_item['c_creatdate'] = tds[4].xpath('string(.)').extract_first()
            c_item['c_expiredate'] = tds[5].xpath('string(.)').extract_first().strip()
            c_item['c_issuer'] = tds[6].xpath('string(.)').extract_first().strip()
            yield c_item

        person_url = response.urljoin(response.meta['urls']['person_url_'])

        yield Request(person_url, callback=self.get_person,
                      cookies=response.meta['cookies'],
                      meta=response.meta, dont_filter=True)

    def get_person(self, response):
        trs = response.xpath('//table/tbody/tr')
        for tr in trs:
            tds = tr.xpath('td')
            p_item = PersonItem()
            p_item['table_name'] = 'jz_person'
            p_item['social_code'] = response.meta['social_code']

            p_item['p_name'] = tds[1].xpath('string(.)').extract_first().strip()
            p_item['p_code'] = tds[2].xpath('string(.)').extract_first()
            p_item['p_ctype'] = tds[3].xpath('string(.)').extract_first()
            p_item['p_ccode'] = tds[4].xpath('string(.)').extract_first()
            p_item['p_profession'] = tds[5].xpath('string(.)').extract_first()

            yield p_item

        progress_url = response.urljoin(response.meta['urls']['progress_url_'])

        yield Request(progress_url, callback=self.get_progress,
                      cookies=response.meta['cookies'],
                      meta=response.meta, dont_filter=True)

    def get_progress(self, response):
        trs = response.xpath('//table/tbody/tr')
        for tr in trs:
            tds = tr.xpath('td')

            p_item = ProgressItem()
            p_item['table_name'] = 'jz_progress'
            p_item['social_code'] = response.meta['social_code']

            p_item['p_code'] = tds[1].xpath('string(.)').extract_first().strip()
            p_item['p_name'] = tds[2].xpath('string(.)').extract_first()
            p_item['p_addr'] = tds[3].xpath('string(.)').extract_first()
            p_item['p_type'] = tds[4].xpath('string(.)').extract_first()
            p_item['p_company'] = tds[5].xpath('string(.)').extract_first()

            yield p_item

