## demo.py

Dit is een toelichting bij `demo.py`. Probeer de onderdelen van `demo.py` te begrijpen. Voeg eventueel extra print-opdrachten toe. Experimenteer met eigen variaties. Je kunt de inhoud van de database ook opvragen en aanpassen door middel van de shell.

De voorbeelden illustreren de flexibiliteit bij het gebruik van documenten, en het gebruik van embedding en referencing.

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

We zorgen ervoor dat beide collecties leeg zijn. Je kunt ook beginnen met een vooraf gevulde database: dat moet je deze drop-opdrachten weglaten. 

```
docenten.drop() # start with empty collections
scholen.drop()
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

*Verschillen tussen Python en MongoDB shell-notatie.* In Python gebruik je de notatie `d["naam"]` voor het selecteren van een veld. In de MongoDB shell en in JavaScript gebruik je daarvoor `d.naam`. Voor de veldnamen in de notatie van een dictionary-waarde moet je altijd quotes gebruiken: `{"naam": "Bart"}` in plaats van `{naam: "Bart"}`, zoals in JavaScript of MongoDB shell.

*Opdracht*: controleer dat een document op deze manier maar éénmaal toegevoegd wordt, door eenzelfde docent-docement meerdere malen toe te voegen via `addDocent`.

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

Embedding komt overeen met het gebruik van een dictionary in een dictionary, wat een normale constructie is in Python:

```
hans = {"naam": "Hans",
        "vak":  "Frans",
        "school": {"naam": "Hyperbolium", 
                   "plaats": "Amsterdam"
                  }
       }
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

Als we bij het opvragen van een docent-document ook de gegevens van de school willen hebben, moeten we daarvoor een extra `find` in de school-collection uitvoeren. Je kunt dit zien als een "uitgeprogrammeerde join".

```
for docent in db.docenten.find():
  school = db.scholen.find_one({"_id": docent["school_id"]})
  docent["school"] = school
  print(docent)
```

Bij de afweging tussen embedding en referencing moet je je afvragen welke combinaties van gegevens vaak gebruikt worden in een toepassing. Door handig gebruik te maken van embedding kun je het aantal collections en het aantal database-opdrachten sterk verminderen.

*Opdracht*: het resultaat van `find_one` is `None`, als er geen document gevonden wordt dat aan het zoekcriterium voldoet. Pas het programma zo aan dat in het docent-document in dat geval geen school-veld ingevuld wordt.

*Opdracht*: voeg een veld `docenten` toe aan elk school-document, en vul dit in via een query op alle docenten in de database.

*Opdracht*: verander de docent-documenten zo dat een docent meerdere scholen kan hebben.
