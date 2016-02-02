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

```
def addDocent(d):
  docenten.replace_one(
    {"naam": d["naam"]},
    d,
    True
  )
```

In Python gebruik je de notatie `d["naam"]` voor het selecteren van een veld. In de Mongo shell en in JavaScript gebruik je daarvoor `d.naam`.

*Opgave*: controleer dat een document op deze manier maar éénmaal toegevoegd wordt, door eenzelfde docent-docement meerdere malen toe te voegen via `addDocent`.

