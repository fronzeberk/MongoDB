from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['RGR2']

for i in range(1, 13):
    print("Месяц", i, ":")
    for st in db.students.find():
        birth_month = st['birthday'].split("/")[1]
        if birth_month == str(i) or (birth_month.startswith("0") and birth_month[1:] == str(i)):
            print(st['name'])
