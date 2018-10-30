# -*- coding: utf-8 -*-
import pymongo

if __name__ == '__main__':
    myclient = pymongo.MongoClient("mongodb://207.246.79.181:27017/")
    mydb = myclient["Exercise"]
    dblist = myclient.list_database_names()
    # dblist = myclient.database_names()
    if "runoobdb" in dblist:
        print("数据库已存在！")