from pymongo import MongoClient
from datetime import datetime

client = MongoClient('localhost', 27017)

db = client.leandro

"""
    The database dates will be imported as string. Since we want to
    to some fancy stuff using dates first convert it to mongo format
"""
print('Converting data_inicio to mongodb date')
converted = 0
for estudante in db.estudantes.find():

    if type(estudante['data_inicio']) != str:
        continue

    estudante['data_inicio'] = datetime.strptime(estudante['data_inicio'], '%Y-%m-%d')
    db.estudantes.save(student)

    converted += 1

print('Done converting. Converted documents: ', converted)