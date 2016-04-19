#!/usr/bin/env python

import urllib, requests
from bottle import route, run
from triggers_json import dic
from elasticsearch import Elasticsearch
import nltk

trigger_list = dic.keys()
print trigger_list

es = Elasticsearch()
stopwords = nltk.corpus.stopwords.words("english")

@route('/<query>', method="GET")
def index(query=""):
	
	filtered_query = [i for i in query.split() if i not in stopwords]	##filtering out stopwpords
	filtered_query_string  = " ".join(filtered_query)
	print filtered_query

	template = [dic[x] for x in filtered_query if x in dic.keys()]
	print template

	query={
   
   "query": {
     "filtered": {
       "query": {
             "multi_match": {
               "query": filtered_query_string,
               "fields": ["description^5", "name^10","val^2"],
               "type": "cross_fields"
             }
         
         
       }
     }
 
   }
 }
	query = es.search(index="ddg", doc_type="cheatsheet", body=query)
	return {"template_type":template, "cheat":query}

run(host='localhost', port=8080,debug=True)