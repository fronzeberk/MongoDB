from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['RGR2']

students = db.students.find()

for st in students:
    last_name = st['name'].split(" ")[0]
    if last_name[0] == "М":
        print(st['name'])
        group_info = db.groups.find_one({'_id': st['group_id']}, {'name': 1, 'direction': 1, '_id': 0})
        print(group_info)
        print()
