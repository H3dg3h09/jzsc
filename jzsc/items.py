# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JzscItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class BasicInfoItem(scrapy.Item):
    table_name = scrapy.Field()

    name = scrapy.Field() # 公司名
    social_code = scrapy.Field() # 公司统一社会信用代码
    legal_re = scrapy.Field() # 法人
    com_type = scrapy.Field() # 注册类型
    province = scrapy.Field() # 属地
    addr = scrapy.Field() #经营地址


class CredentialsItem(scrapy.Item):
    table_name = scrapy.Field()

    social_code = scrapy.Field() # 公司统一社会信用代码
    c_type = scrapy.Field() # 资质类别
    c_code = scrapy.Field() # 资质证书号
    c_name = scrapy.Field() # 资质名称
    c_creatdate = scrapy.Field() # 发证日期
    c_expiredate = scrapy.Field() # 有效期
    c_issuer = scrapy.Field() # 颁发者


class PersonItem(scrapy.Item):
    table_name = scrapy.Field()

    social_code = scrapy.Field()  # 公司统一社会信用代码
    p_name = scrapy.Field()  # 姓名
    p_code = scrapy.Field()  # 身份证号
    p_ctype = scrapy.Field()  # 注册类别
    p_ccode = scrapy.Field() # 注册号
    p_profession = scrapy.Field() # 注册专业


class ProgressItem(scrapy.Item):
    table_name = scrapy.Field()
    social_code = scrapy.Field()  # 公司统一社会信用代码

    p_code = scrapy.Field()  # 项目编码
    p_name = scrapy.Field()  # 项目名称
    p_addr = scrapy.Field()  # 项目属地
    p_type = scrapy.Field() # 项目类别
    p_company = scrapy.Field() # 建设单位