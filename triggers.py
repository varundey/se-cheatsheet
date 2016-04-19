#!/usr/bin/env python

import json
from pymongo import MongoClient

file = open("triggers_json.json","r")
triggers = json.load(file)

cl = MongoClient()
db = cl['cheatsheet']
collection = db['triggers']
collection.insert(triggers)