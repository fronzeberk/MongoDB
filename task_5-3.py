from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['RGR2']

teacher_students = {}

for m in db.marks.find():
    teacher = m['teacher']
    student = str(m['student'])    
    if teacher in teacher_students:
        teacher_students[teacher].add(student)
    else:
        teacher_students[teacher] = {student}
        
for teacher, students in teacher_students.items():
    print(f"{teacher}: {len(students)}")
