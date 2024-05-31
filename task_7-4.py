from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['RGR2']

def get_subj_from_sched(schedule_id):
    schedule = db.schedule.find_one({'_id': schedule_id}, {'subject': 1, '_id': 0})
    if schedule:
        return schedule['subject']
    return None

students = db.students.find()
attendances = list(db.attendence.find({'attendence': True}))

for student in students:
    hours_count = {}
    for at in attendances:
        subject = get_subj_from_sched(at['schedule'])
        if subject:
            if subject in hours_count:
                hours_count[subject] += 1.5
            else:
                hours_count[subject] = 1.5

    print(student['name'])
    print(hours_count)

print(hours_count)
