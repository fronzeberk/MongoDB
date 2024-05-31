from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['RGR2']

subject_marks = {}

for m in db.marks.find():
    if m['mark'] > 2:
        if m['subject'] in subject_marks:
            subject_marks[m['subject']].append(m['mark'])
        else:
            subject_marks[m['subject']] = [m['mark']]

sub_avg = {}

for subject, marks in subject_marks.items():
    sub_avg[subject] = sum(marks) / len(marks)

print(sub_avg)
