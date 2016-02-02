import pymongo

client = pymongo.MongoClient()

# use the 'test' database:
db = client.test # or: client["test"]

# show all collections:
print("Collections:")
print(db.collection_names(include_system_collections=False))

# use the 'docenten' en "scholen" collection:
docenten = db.docenten # or: db["docenten"]
scholen = db.scholen

docenten.drop() # start with empty collections
scholen.drop()

def addDocent(d):
  docenten.replace_one(
    {"naam": d["naam"]},
    d,
    True
  )

def addSchool(s):
  scholen.replace_one(
    {"naam": s["naam"]},
    s,
    True
  )

bakker = {"naam": "Bart Bakker", "vak": ["Informatica", "Natuurkunde"]}
jansen = {"naam": "Johan Jansen", "vak": "Informatica"}
klepper = {"naam": "Kees Klepper", "vak": ["Informatica", "Wiskunde"]}

addDocent(bakker)
addDocent(jansen)
addDocent(klepper)

# show all documents in this collection:
print("Alle docenten:")
for docent in docenten.find():
  print(docent)

# show all documents with the specified property:
print("Informatica-docenten:")
for docent in docenten.find({"vak": "Informatica"}):
  print(docent)

# show all documents with the specified property:
print("Natuurkunde-docenten:")
for docent in docenten.find({"vak": "Natuurkunde"}):
  print(docent)


# update a document
#collection.update_one(
#  {"naam": "Bart Bakker"},
#  {"$set": {"vak": ["Informatica", "Wiskunde", "ANW"]}}

hyper = {"naam": "Hyperbolium Lyceum", "plaats": "Haarlem"}
jobs = {"naam": "Gymnasium Jobsianum", "plaats": "Amsterdam"}


addSchool(hyper)
addSchool(jobs)

def setSchool(d, s):
  docenten.update_one(
    {"naam": d["naam"]},
    {"$set": {"school": s}},
    True
  )

bakker["school"] = hyper
addDocent(bakker)

setSchool(jansen, hyper)
setSchool(klepper, jobs)

# show all documents in this collection:
print("Alle docenten:")
for docent in docenten.find():
  print(docent)

# extend embedding with referencing

addSchool(hyper)
addSchool(jobs)
print("Alle scholen:")
for school in scholen.find():
  print(school)

def addSchoolRef(d):
  s = db.scholen.find_one({"naam": d["school"]["naam"]})
  print("school:")
  print(s)
  db.docenten.update_one(
    {"naam": d["naam"]},
    {"$set": {"school.id": s["_id"]}},
    True
  )

for docent in db.docenten.find():
  addSchoolRef(docent)

print("\nAlle scholen:")
for school in scholen.find():
  print(school)


# show all documents in this collection:
print("\nAlle docenten:")
for docent in docenten.find():
  print(docent)

db.scholen.update(
  {"naam": hyper["naam"]},
  {"$set": {"betapartner": "True"}}
)

db.scholen.update(
  {"naam": jobs["naam"]},
  {"$set": {"betapartner": "False"}}
)

print("\nDocenten:")
for docent in db.docenten.find():
  school = db.scholen.find_one({"_id": docent["school"]["id"]})
  docent["school"]["betapartner"] = school["betapartner"]
#  del docent["school"]["id"]
  print(docent)
