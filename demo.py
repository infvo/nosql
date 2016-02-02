import pymongo

client = pymongo.MongoClient()

# use the 'test' database:
db = client.test # or: client["test"]

# show all collections:
print(db.collection_names(include_system_collections=False))

# use the 'docenten' collection:
collection = db.docenten # or: db["docenten"]

# show all documents in this collection:
for docent in collection.find():
  print(docent)
