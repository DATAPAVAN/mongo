import pymongo

client = pymongo.MongoClient("mongodb+srv://asadhya:7550202316@asadhya.a0imlza.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d={'name':'pavan','emailid':'kkbk@gmail.com'}

db1=client['mongotest1']
coll=db1['test']
coll.insert_one(d)
record = coll.find()
for i in record:
    print(i)
coll.find.prettyprint()



