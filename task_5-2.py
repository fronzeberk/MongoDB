from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['RGR2']

pipeline = [
    {
        '$group': {
            '_id': {'group': '$group', 'subject': '$subject'},
            'subjectCount': {'$sum': 1}
        }
    },

    {
        '$sort': {'subjectCount': -1}
    },
    
    {
        '$limit': 1
    }
]

result = db.schedule.aggregate(pipeline)

for doc in result:
    print(doc)
