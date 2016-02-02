## NoSQL - MongoDB

De opdrachten in dit repository zijn bedoeld als eerste oefeningen met MongoDB, als voorbeeld van een NoSQL database.

## Installeren

### Cloud9

* maak een nieuw repository aan, via "clone from git", met de git-URL van dit repository.
* geef deze readme weer als preview: selecteer `readme.md`, en selecteer via het dropdown-menu "preview". (Of, open `readme.md`, en selecteer in het menu bovenin "Preview".)

#### MongoDB

MongoDB is standaard geïnstalleerd op Cloud9. Op de volgende manier activeer je mongodb:

* zie: https://docs.c9.io/docs/setting-up-mongodb
* voor de onderstaande opdrachten één voor één uit in een terminal-venster (rechts onderin).

```shell
$ mkdir data
$ echo 'mongod --bind_ip=$IP --dbpath=data --nojournal --rest "$@"' > mongod
$ chmod a+x mongod
```

* open een nieuw terminal-venster (onderaan), en start daarin mongodb:
* `$ mongod`
* laat dit programma actief in dit venster; gebruik voor andere opdrachten een ander terminal-venster.
* in dit terminal-venster krijg je de mededelingen van de database-driver.

* Open een nieuwe terminal-venster, en start de mongodb-shell, met het commando:
* `$ mongo`
* Je kunt daarin mongodb-shell opdrachten geven, bijvoorbeeld:
* `> show databases`

## Python

We hebben de volgende python-onderdelen nodig:

* `pymongo`: de library om vanuit Python MongoDB aan te sturen ("driver").
* `web.py`: een eenvoudig framework voor het maken van websites vanuit Python

* `> sudo pip install pymongo`
* `> sudo pip install web.py`
* `> python webdemo.py`
