#!/usr/bin/env/ python
from elasticsearch import Elasticsearch
es = Elasticsearch()
a={
   
   "query": {
     "filtered": {
       "query": {
             "multi_match": {
               "query": "french phrases",
               "fields": ["description^5", "name^10","val^2"],
               "type": "cross_fields"
             }
         
         
       },
       "filter": {
         "term": {
           "template_type": "language"
         }
       }
     }
 
   }
 }

x = es.search(index="ddg", doc_type="cheatsheet", body=a)
print x
