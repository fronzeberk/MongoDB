from pymongo import MongoClient
from datetime import datetime

client = MongoClient('mongodb://localhost:27017/')
db = client['RGR2']

current_month = datetime.now().month

for st in db.students.find():
    birth_month = int(st['birthday'].split("/")[1])
    if birth_month == current_month:
        print(st['name'])
