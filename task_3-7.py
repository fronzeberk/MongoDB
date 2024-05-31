from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['RGR2']

def count_el(object):
    counter = 0
    for el in object:
        counter += 1
    return counter

for gr in db.groups.find():
    print(gr['name'])
    print(gr['direction'])
    budget_students_count = count_el(db.students.find({'group_id': gr['_id'], 'budget': True}))
    non_budget_students_count = count_el(db.students.find({'group_id': gr['_id'], 'budget': False}))
    print("Students on budget:", budget_students_count)
    print("Students without budget:", non_budget_students_count)
    print()
