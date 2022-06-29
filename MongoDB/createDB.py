import pymongo
str = input("MongoDB password:")  #"1qazxsw2!QAZXSW%"
str1 = "mongodb+srv://imi78:"+str+"40@cluster0.1mwqk.mongodb.net/mydb?retryWrites=true&w=majority"
client = pymongo.MongoClient(str1)

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

# for creating multiple collections use:

# mydict = [
#    {"_id": "101", "name": "Ivan", "age": "26", "city": "Sofia"},
#    {"_id": "102", "name": "Dragan", "age": "27", "city": "Plovdiv"},
#    {"_id": "103", "name": "Petkan", "age": "28", "city": "Varna"}
# ]
# coll.insert_many(mydict)

# prints all items from the collections
for item in coll.find():
  print(item)

# printing all the items in the collections without  the "_id".
num = 1
for item in coll.find():
  print(str(num) + " " + "Collection")
  print("-----------------")
  for k,v in item.items():
    if k != "_id":
      print(f"{k} : {v}")
  num += 1
  print()