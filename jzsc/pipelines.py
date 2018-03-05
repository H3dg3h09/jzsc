# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import logging
from .static import Db
import codecs
db = Db.init_db()

class JzscPipeline(object):

    def process_item(self, item, spider):

        table_name = item.pop('table_name')
        try:
            i = db.insert_data(table_name, item)
        except AttributeError:
            logging.log(logging.ERROR, '{name} insert to {table} failed.'.format(name=item['name'], table=table_name))
            print( '{name} insert to {table} failed.'.format(name=item['name'], table=table_name))
        else:
            logging.log( logging.INFO, 'id : {i}'.format(i=i))
            print('id : {i}'.format(i=i))


        return item
