import pymongo

client = pymongo.MongoClient()

# use the 'test' database:
db = client.test # or: client["test"]

# show all collections:
print("Collections:")
print(db.collection_names(include_system_collections=False))

# use the 'docenten' collection:
collection = db.docenten # or: db["docenten"]

# show all documents in this collection:
print("Alle docenten:")
for docent in collection.find():
  print(docent)

# show all documents with the specified property:
print("Informatica-docenten:")
for docent in collection.find({"vak": "Informatica"}):
  print(docent)

# show all documents with the specified property:
print("Natuurkunde-docenten:")
for docent in collection.find({"vak": "Informatica"}):
  print(docent)
