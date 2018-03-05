#!/usr/bin/env python
# -*- coding: utf-8 -*-
from jzsc.settings import DB
import six

class Db():

    def __init__(self, host, port,user, password, db):
        import pymysql
        self._cnx = pymysql.connect(host=host, port=port, user=user, password=password, db=db, charset="utf8")
        self._cursor = self._cnx.cursor()

    def insert_data(self, table_name, data):
        '''
        :param table_name: str
        :param data: dict
        :return: bool
        '''

        col_str = ''
        row_str = ''
        for key in data.keys():
            col_str = col_str + " " + key + ","
            row_str = "{}'{}',".format(row_str,
                                       data[key] if "'" not in data[key] else data[key].replace("'", "\\'"))
            sql = "INSERT INTO {} ({}) VALUES ({}) ON DUPLICATE KEY UPDATE ".format(table_name, col_str[1:-1],
                                                                                    row_str[:-1])
        for (key, value) in six.iteritems(data):
            sql += "{} = '{}', ".format(key, value if "'" not in value else value.replace("'", "\\'"))
        sql = sql[:-2]

        self._cursor.execute(sql)  # 执行SQL
        i = self._cnx.insert_id()
        try:
            self._cnx.commit()  # 写入操作
        except AttributeError as e:
            raise e
        else:
            return i


    @classmethod
    def init_db(cls):
        host = DB.get('DATABASE_HOST', '')
        user = DB.get('DATABASE_USER', '')
        password = DB.get('DATABASE_PASSWORD', '')
        db = DB.get('DATABASE_DB', '')
        port = DB.get('DATABASE_PORT', '')
        return cls(host=host, port=port, user=user, password=password, db=db)
