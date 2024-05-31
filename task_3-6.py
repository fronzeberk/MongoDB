from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['RGR2']

def count_el(object):
    counter = 0
    for el in object:
        counter += 1
    return counter

direction_count = {}

for gr in db.groups.find():
    students_in_group = count_el(db.students.find({'group_id': gr['_id']}))
    if gr['direction'] in direction_count:
        direction_count[gr['direction']] += students_in_group
    else:
        direction_count[gr['direction']] = students_in_group

print(direction_count)

