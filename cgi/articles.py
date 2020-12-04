#!/usr/bin/python
#coding=utf-8

import re
import sys
import json
import bson
import pymongo
import cgi, cgitb

reload(sys)
sys.setdefaultencoding("utf-8")

form = cgi.FieldStorage()

formData = {}
for item in form:
    formData[item] = form.getvalue(item)

print "Content-type:text/html"
print 

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client.coolstack
col = db.article
datas = {}

if formData["type"] == "title":
    datas["title"] = []
    datas["id"] = []
    datas["class"] = []
    for data in col.find({},{"class": 1, "title": 1, "_id": 1}):
        datas["title"].append(data["title"])
        datas["id"].append(str(data["_id"]))
        datas["class"].append(data["class"])
    print(json.dumps(datas))

elif formData["type"] == "article":
    try:
        for data in col.find({"_id": bson.ObjectId(formData["id"])}, {"_id": 0}):
            datas = data
    except Exception as e:
        print(e)
    else:
        print(json.dumps(datas))

elif formData["type"] == "search":
    datas["title"] = []
    datas["id"] = []
    try:
        for data in col.find({"title": {"$regex": re.compile(formData["title"])}}).sort("title"):
            datas["title"].append(data["title"])
            datas["id"].append(str(data["_id"]))
    except Exception as e:
        print(e)
    else:
        print(json.dumps(datas))