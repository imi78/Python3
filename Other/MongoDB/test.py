import pymongo
client = pymongo.MongoClient("mongodb+srv://imi78:<password>@cluster0.1mwqk.mongodb.net/mydb?retryWrites=true&w=majority")

# Get the available databases
db = client.list_database_names()
print(db)

# create instance of the DB
db = client["mydb"]

# create instance of the available collections anbd puts it in a variable
coll = db["test"]

# Add item in the database

# mydict = { "name": "John", "address": "Highway 37" }
# coll.insert_one(mydict)

# prints all items from the collections
for item in coll.find():
  print(item)

# printing all the items in the collections.
num = 1
for item in coll.find():
  print(str(num) + " " + "Collection")
  print("-----------------")
  for k,v in item.items():
    if k != "_id":
      print(f"{k} : {v}")
  num += 1
  print()