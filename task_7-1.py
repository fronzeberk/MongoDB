from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['RGR2']

subject = "Этика"
count = 0

schedules = db.schedule.find({'subject': subject})

for sc in schedules:
    attendances = db.attendence.find({'schedule': sc['_id']})
    for at in attendances:
        if at['attendence'] == True:
            count += 1

print(count)
