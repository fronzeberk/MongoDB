from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['RGR2']

for t in db.teachers.find():
    print(t['subject'] + " " + t['name'])
    groups = db.schedule.find({'subject': t['subject']}, {'group': 1, '_id': 0})
    for gr in groups:
        group_name = db.groups.find_one({'_id': gr['group']}, {'name': 1, '_id': 0})['name']
        print(group_name)    
    print()
