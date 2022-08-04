import pymongo
client = pymongo.MongoClient("mongodb+srv://nithaskumar:Changeme1!@cluster0.a9sba.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)


d={
    'name':'Nitha',
    'email':'mail44nitha@gmail.com',
    'surname':'S gitKumar'
}
db1=client['mongotest']
coll=db1['test']
coll.insert_one(d)