#!/usr/bin/python
#coding=utf-8

import os
import sys
import time
import pymongo

reload(sys)
sys.setdefaultencoding("utf8")

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client.coolstack
col = db.article

for dir in os.listdir("../articles"):
    path = unicode("../articles/"+dir , "utf8")
    for file in os.listdir(path):
        mydict = {}
        if os.path.splitext(file)[1] == ".md":
            myquery = {"title": os.path.splitext(file)[0]}
            x = col.find_one(myquery)
            if x == None:
                mydict["title"] = os.path.splitext(file)[0]
                mydict["content"] = open("../articles/"+dir+"/"+file, "r").read()
                mydict["class"] = dir
                #mydict["tag"] = "C++"
                mydict["date"] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 
                col.insert_one(mydict)
            else:
                mydict["$set"] = {}
                mydict["$set"]["content"] = open("../articles/"+dir+"/"+file, "r").read()
                col.update_one(myquery, mydict)
                
