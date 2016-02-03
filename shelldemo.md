## MongoDB shell voorbeelden

Met de MongoDB shell kun je interactief database-opdrachten geven. Dit helpt bij het leren werken met de opdrachten van MongoDB. Je werkt hiermee in een terminal-window.

* tutorial: https://docs.mongodb.org/getting-started/shell/
* handleiding: https://docs.mongodb.org/manual/mongo/
* kort overzicht: https://docs.mongodb.org/manual/reference/mongo-shell/

*Tip*: met de pijltjes-toetsen kun je de opdrachten uit de historie opvragen; deze kun je ook aanpassen en opnieuw laten uitvoeren, bijvoorbeeld als je een tikfout gemaakt hebt.

`$ mongo` - start de shell (in een terminal-window).

`> show databases` - overzicht van aanwezige databases.

`> use test` - we werken met de "test" database.

`> show collections` - we werken met de "test" database.

Toevoegen van een docent-document:

```
> db.docenten.insert({
... naam: "Bart Bakker",
... vak: "Informatica"
})
```

Opvragen van alle documenten in de docenten-collection:

```
> db.docenten.find()
```

*Opdracht*: voeg de docent-documenten toe:

```
{naam: "Kees Klepper", vak: ["Informatica", "Wiskunde"]}
{naam: "Frans Filmer", vak: ["Wiskunde"]}
{naam: "Jos Jansen", vak: "Engels"}
```

en vraag een overzicht van alle documenten.

*Merk op* dat we hier verschillende vormen gebruiken voor het veld "vak".

### Find

Opvragen van alle informatica-docenten:

```
> db.docenten.find({vak: "Informatica"})
```

Opvragen van docenten die wiskunde **en** informatica geven:

```
> db.docenten.find({vak: "Informatica", vak: "Wiskunde"})

```

Docenten die wiskunde **of** engels geven (via `$or` met een rij alternatieven):

```
> db.docenten.find(
... {$or: [{vak: "Wiskunde"},
...        {vak: "Engels"}]
... })
```

### Update

Veranderen van een veld:

```
> db.docenten.update( 
... {naam: "Jos Jansen"}, 
... {$set: {vak: ["Engels"]} } 
... )
```
De eerste parameter selecteert het document (als bij "find"), de tweede parameter is een update-commando, hier `$set` met een rij velden met hun nieuwe waarde.

*Opmerking*: het is in dit geval handiger om voor alle documenten een lijst (array) te gebruiken voor het veld "vak". Je kunt de overgang van een enkel element naar een lijst soepel later verlopen.

*Opdracht*: gebruik deze `update` om voor een docent de eigenschap `school` toe te voegen: een veld met een (sub)document als waarde: `{naam: "Christiaan Huygens", plaats: "Groningen"}`.

*Opdracht*: verander de plaats van de school van Groningen naar Eindhoven. *Hint*: gebruik hiervoor de veldnaam voor een embedded document: `school.naam`.

### Upsert

Een insert-opdracht voegt altijd een nieuw document toe, ook als de waarden van de velden gelijk zijn. (*Probeer dit.*) 

Als je dat niet wilt, kun je een update-opdracht gebruiken met de parameter: `upsert: true`. Dit is een update van een bestaand document, of, als dat er niet is, een insert van een nieuw document.

* https://docs.mongodb.org/manual/reference/method/db.collection.update

```
> db.docenten.update(
... {naam: "Hans Hoekstra"},
... {naam: "Hans Hoekstra", vak: ["Informatica", "Nederlands"]},
... {upsert: true}
... )
```

*Opdracht:* controleer dat het document maar één keer toegevoegd wordt door deze opdracht (via de historie: pijltje terug) meerdere malen uit te voeren. 
