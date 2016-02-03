## NoSQL - MongoDB

De opdrachten in dit repository zijn bedoeld als eerste oefeningen met MongoDB, als voorbeeld van een NoSQL database.

## Installeren

### Cloud9

* maak een nieuw repository aan, via "clone from git", met de URL van dit repository: `https://github.com/infvo/nosql.git`
* geef deze readme weer als preview: selecteer `readme.md`, en selecteer via het dropdown-menu "preview". (Of, open `readme.md`, en selecteer in het menu bovenin "Preview".)

#### MongoDB

MongoDB is standaard geïnstalleerd op Cloud9. Op de volgende manier activeer je mongodb:

* zie: https://docs.c9.io/docs/setting-up-mongodb
* open een nieuw terminal-venster (onderaan), en voer daarin de onderstaande opdrachten één voor één uit:

```shell
$ mkdir data
$ echo 'mongod --bind_ip=$IP --dbpath=data --nojournal --rest "$@"' > mongod
$ chmod a+x mongod
$ mongod
```

* houd het programma `mongod` actief in dit venster; gebruik voor andere opdrachten een ander terminal-venster.
* in dit terminal-venster krijg je de mededelingen van de database-driver.

Je kunt database-opdrachten uitvoeren via de mongodb-shell. Open hiervoor een nieuw terminal-venster, en start daarin de mongodb-shell via het commando: 

* `$ mongo`

Daarn kun je mongodb-shell opdrachten geven, bijvoorbeeld: 

* `> show databases`

### Python

We hebben de volgende python-onderdelen nodig:

* `pymongo`: de library om vanuit Python MongoDB aan te sturen ("driver").
* `web.py`: een eenvoudig framework voor het maken van websites vanuit Python

Deze onderdelen kun je installeren door middel van de volgende shell-opdrachten:

```shell
$ sudo pip install pymongo
$ sudo pip install web.py
```

Je kunt de werking van `web.py` controleren via:

```
$ python webdemo.py
```
