from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['RGR2']

students = db.students.find()
groups = db.groups.find()

for gr in groups:
    students_by_group = db.students.find({'group_id': gr['_id']}, {'name': 1, 'budget': 1, '_id': 0}).sort('name', 1)
    print("Группа:", gr['name'])
    for student in students_by_group:
        print(student)
