from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['RGR2']

students_marks = {}

for m in db.marks.find():
    student = db.students.find_one({'_id': m['student']}, {'name': 1, '_id': 0})['name']
    if student in students_marks:
        students_marks[student].add(m['mark'])
    else:
        students_marks[student] = {m['mark']}

great_student_counter = 0

for student, marks in students_marks.items():
    if len(marks) == 1 and 2 in marks:
        great_student_counter += 1
        print(student)

if great_student_counter == 0:
    print("There are no such students")
