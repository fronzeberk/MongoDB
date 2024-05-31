from pymongo import MongoClient
from datetime import datetime

client = MongoClient('mongodb://localhost:27017/')
db = client['RGR2']

current_date = datetime.now()

for st in db.students.find():
    birthday = datetime.strptime(st['birthday'], '%d/%m/%Y')
    date_diff = (current_date - birthday).days // 365
    print({
        'Студент': st['name'],
        'Возраст': date_diff
    })
