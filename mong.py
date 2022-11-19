import pymongo
client = pymongo.MongoClient("mongodb+srv://rehanahmed:Rocky420@rehan.uwdoiex.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name":"rehan",
    "city":"gaya",
    "roll":"thirty",
    "tick":"load"
}
db1= client['mongotest']
coll = db1['test']
coll.insert_one(d)


