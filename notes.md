## Opmerkingen

Python-JSON: `json.dumps` kan `ObjectId('56b061c7f6e80657abb6440e')` niet in JSON omzetten.

Python-pymongo: voor het toevoegen van een document moet je in plaats van `update`, `replace` gebruiken, met `upsert = True`.

Documenten aanpassen:

```
for d in db.docenten.find():
  if not isinstance(d["vak"], list):
    collection.update_one(
      {"_id": d["_id"]},
      {"$set": {"vak": [d["vak"]]}}
    )
```
