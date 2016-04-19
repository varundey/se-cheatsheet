#!/usr/bin/env python

from elasticsearch import Elasticsearch
es = Elasticsearch()
import json
import os

x= os.listdir("/home/varun/Desktop/git/zeroclickinfo-goodies/share/goodie/cheat_sheets/json")
li=[]
for xx in x:
	try:
		if ".json" in xx:
			js = json.loads(open("/home/varun/Desktop/git/zeroclickinfo-goodies/share/goodie/cheat_sheets/json/"+xx,"r").read())
			print xx
			res = es.index(index="ddg", doc_type='cheatsheet', id=xx, body=js)
			print(res['created'])
	except Exception as e:
		li.append(xx+str(e))
print li