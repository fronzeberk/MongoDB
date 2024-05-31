from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/') 
db = client['RGR2']

passet_students = set()

for m in db.marks.find():
    if m['mark'] > 2:
        student = db.students.find_one({'_id': m['student']}, {'name': 1, '_id': 0})
        if student:
            passet_students.add(student['name'])

print(passet_students)
