# Examenopdrachtdecember2025
 Python-examenopdracht december 2025 en herexamen augustus 2026


## Doel van de applicatie

Deze Python-applicatie beheert een boekenlijst met bijbehorende locaties.



## Technologie

* Python 3
* SQLite
* CSV



## Bibliotheken

De applicatie gebruikt enkel standaardonderdelen van Python en geen externe packages.



## Functies

De applicatie kan volgende zaken:

- boeken toevoegen

- boeken bekijken

- boeken aanpassen

- boeken verwijderen

- locaties toevoegen

- locaties bekijken

- locaties aanpassen

- locaties verwijderen

- export van de boekenlijst naar een CSV-bestand



## Vereisten


Er zijn geen externe packages nodig.
De applicatie gebruikt enkel modules die standaard aanwezig zijn, zoals:

- sqlite3

- csv





## Hoe uitvoeren

1. Kloon de repository of download de code.

2. Ga naar de projectmap.

3. Maak eventueel een virtuele omgeving aan:
python -m venv .venv

4. Voer de code uit:
python Examenopdrachtdecember2025.py





## Klassen



### Domeinklassen

De domeinklassen stellen de objecten uit het domein van de applicatie voor.

1. De klasse Boek bevat:

   1. boek\_id
   2. titel
   3. auteur
   4. uitgave\_jaar

2. De klasse Locatie bevat:

   1. boek\_id
   2. naam\_depot
   3. plank

De domeinklassen bevatten geen rechtstreekse databasecode.



### Repositoryklassen

De repositoryklassen zorgen voor de communicatie met de SQLite-database.

`BoekRepository` beheert de databasebewerkingen voor boeken:

- boeken toevoegen

- boeken bekijken

- boeken aanpassen

- boeken verwijderen

- boeken exporteren naar CSV


`LocatieRepository` beheert de databasebewerkingen voor locaties:

- locaties toevoegen

- locaties bekijken

- locaties aanpassen

- locaties verwijderen





## Structuur van de database


De database bestaat uit 2 tabellen:
---

```sql

CREATE TABLE "Boeken" (
	"id"	INTEGER,
	"Titel"	TEXT NOT NULL,
	"Auteur"	TEXT NOT NULL,
	"UitgaveJaar"	INTEGER NOT NULL,
	PRIMARY KEY("id")
);

```





```sql

CREATE TABLE "Locatie" (
	"id"	INTEGER,
	"boekID"	INTEGER,
	"NaamDepot"	TEXT NOT NULL,
	"Plank"	INTEGER,
	FOREIGN KEY("boekID") REFERENCES "Boeken"("id"),
	PRIMARY KEY("id")
);

```

