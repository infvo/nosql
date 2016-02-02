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
print("\nAlle docenten:")
for docent in docenten.find():
  print(docent)

# show all documents with the specified property:
print("\nInformatica-docenten:")
for docent in docenten.find({"vak": "Informatica"}):
  print(docent)

# show all documents with the specified property:
print("\nNatuurkunde-docenten:")
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
print("\nAlle docenten:")
for docent in docenten.find():
  print(docent)

# extend embedding with referencing

addSchool(hyper)
addSchool(jobs)
print("Alle scholen:")
for school in scholen.find():
  print(school)

def addSchoolRef(docent, schoolnaam):
  school = db.scholen.find_one({"naam": schoolnaam})
#  print("school:")
#  print(school)
  db.docenten.update_one(
    {"naam": docent["naam"]},
    {"$set": {"school_id": school["_id"]}},
    True
  )

addSchoolRef(bakker, hyper["naam"])
addSchoolRef(jansen, hyper["naam"])
addSchoolRef(klepper, jobs["naam"])

# show all documents in this collection:
print("\nAlle docenten met school-id:")
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

print("\nAlle docenten met hun school:")
for docent in db.docenten.find():
  school = db.scholen.find_one({"_id": docent["school_id"]})
  docent["school"] = school
  print(docent)
