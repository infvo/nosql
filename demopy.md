## demo.py

Voor het gebruik van `pymongo`, zie:

* https://docs.mongodb.org/getting-started/python/client/
* https://api.mongodb.org/python/current/

Voordat je de collections kunt gebruiken, moet je eerst een verbinding met mongodb maken, en de database selecteren (hier de database "test"):

```python
client = pymongo.MongoClient()
db = client.test
```

We gebruiken in dit voorbeeld twee collections:

```python
docenten = db.docenten
scholen = db.scholen
```

Voor het toevoegen van een document gebruiken we `replace_one`, een variant van `update`, in plaats van `insert_one`, met `upsert=True`. Op deze manier voorkomen we dat er meerdere documenten met dezelfde naam toegevoegd worden.

```python
def addDocent(d):
  docenten.replace_one(
    {"naam": d["naam"]},
    d,
    True
  )
```

In Python gebruik je de notatie `d["naam"]` voor het selecteren van een veld. In de Mongo shell en in JavaScript gebruik je daarvoor `d.naam`.

*Opgave*: controleer dat een document op deze manier maar éénmaal toegevoegd wordt, door eenzelfde docent-docement meerdere malen toe te voegen via `addDocent`.

### Embedding

We kunnen een subdocument "embedden", direct bij de definitie van het document, voor het invoeren ervan in de database:

```python
bakker["school"] = hyper
addDocent(bakker)
```

We kunnen dit ook achteraf doen, door middel van een `update` opdracht met een `$set` commando:


```python
def setSchool(d, s):
  docenten.update_one(
    {"naam": d["naam"]},
    {"$set": {"school": s}},
    True
  )
  
setSchool(jansen, hyper)
setSchool(klepper, jobs)
```

### Referencing

Een alternatief voor embedding is referencing: we gebruiken dan een verwijzing naar het betreffende document (meestal in een andere collection).

```python
def addSchoolRef(docent, schoolnaam):
  school = db.scholen.find_one({"naam": schoolnaam})
  db.docenten.update_one(
    {"naam": docent["naam"]},
    {"$set": {"school_id": school["_id"]}},
    True
  )

addSchoolRef(bakker, hyper["naam"])
addSchoolRef(jansen, hyper["naam"])
addSchoolRed(klepper, jobs["naam"])
```

*Opmerking:* de docent-documenten in de database bevatten nog steeds een deel van de school-gegevens als embedded document. Een dergelijke gedeeltelijke embedding kan handig zijn als het gegevens betreft die vaak nodig zijn in het omvattende document. Als deze gegevens bovendien niet veranderen (zoals de naam en plaats van de school), dan is er nauwelijks een risico op inconsistentie in de database.


Bij de afweging tussen embedding en referencing moet je je afvragen welke gegevens vaak opgevraagd worden bij een 

*Opdracht*: voeg een veld `docenten` toe aan elk school-document, en vul dit in via een query op alle docenten in de database.
