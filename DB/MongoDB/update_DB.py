import pymongo
client = pymongo.MongoClient("mongodb+srv://imi78:<password>@cluster0.1mwqk.mongodb.net/mydb?retryWrites=true&w=majority")

# create instance of the DB
db = client["mydb"]

# create instance of the available collections anbd puts it in a variable
coll = db["test"]

filter = {"name": "Peter"}
new_values = {"$set": {"age": 50}}

# updates the collection with the given filter with new the news values
# adds a new field if it doesn't exist
coll.update_one(filter, new_values)

# update all items in a collection with a new entry - the empty filter means all items in the collection will be updated
coll.update_many({}, {"$set" : {"phone": "0123456789"}})

# remove an entry from all items in the collection
coll.update_many({}, {"$unset" : {"phone": "0123456789"}})