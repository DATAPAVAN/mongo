import pymongo

client = pymongo.MongoClient("mongodb+srv://asadhya:7550202316@asadhya.a0imlza.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)
db1=client['mongotest1']
coll=db1['test']
data =  [
        {
            "item": "canvas",
            "qty": 100,
            "size": {"h": 28, "w": 35.5, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "journal",
            "qty": 25,
            "size": {"h": 14, "w": 21, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "mat",
            "qty": 85,
            "size": {"h": 27.9, "w": 35.5, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "mousepad",
            "qty": 25,
            "size": {"h": 19, "w": 22.85, "uom": "cm"},
            "status": "P",
        },
        {
            "item": "notebook",
            "qty": 50,
            "size": {"h": 8.5, "w": 11, "uom": "in"},
            "status": "P",
        },
        {
            "item": "paper",
            "qty": 100,
            "size": {"h": 8.5, "w": 11, "uom": "in"},
            "status": "D",
        },
        {
            "item": "planner",
            "qty": 75,
            "size": {"h": 22.85, "w": 30, "uom": "cm"},
            "status": "D",
        },
        {
            "item": "postcard",
            "qty": 45,
            "size": {"h": 10, "w": 15.25, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "sketchbook",
            "qty": 80,
            "size": {"h": 14, "w": 21, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "sketch pad",
            "qty": 95,
            "size": {"h": 22.85, "w": 30.5, "uom": "cm"},
            "status": "A",
        },
    ]
coll.insert_many(data)
#e=coll.find({'status':{"$in":["A","p"]}})
#f=coll.find({'status':{"$gt":"C"}})
#g=coll.find({'satus':{'$gte':'C'}})
#q=coll.find({'item':'sketchpad','qty':{"$gt":75}})
#q=coll.find({"$or":[{'item':'sketchpad'},{'qty':{"$gte":75}}]})
#coll.update_one({'item':'canvas'},{"$set":{'item':'asadhya'}})
#q=coll.find({'item':'asadhya'})
#coll.delete_many({'item':'asadhya'})
#q=coll.find()
#h=coll.find({'item':'sketchpad','qty':85})

for i in q:
     print(i)


