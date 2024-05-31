from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['RGR2']

def get_group(student_id):
    student = db.students.find_one({'_id': student_id}, {'group_id': 1, '_id': 0})
    if student:
        group = db.groups.find_one({'_id': student['group_id']}, {'name': 1, '_id': 0})
        if group:
            return group['name']
    return None

groups_marks = {}

for m in db.marks.find():
    student_group = get_group(m['student'])
    if student_group:
        if student_group in groups_marks:
            groups_marks[student_group].append(m['mark'])
        else:
            groups_marks[student_group] = [m['mark']]

groups_avg = {group: sum(marks) / len(marks) for group, marks in groups_marks.items()}

sortable = sorted(groups_avg.items(), key=lambda x: x[1], reverse=True)

if sortable:
    print(sortable[0])
