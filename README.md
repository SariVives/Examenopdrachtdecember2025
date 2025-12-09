# -*- coding: utf-8 -*-
"""
READ.ME Examenopdrachtdecember2025
"""

## Doel van de applicatie
Deze Python-applicatie beheert een boekenlijst met bijbehorende locaties. 
Gebruikers kunnen boeken toevoegen, de volledige lijst bekijken, locaties beheren en een CSV-rapport exporteren.

##Technologie
Python 

##Bibliotheken
(zie requirements.txt)
Omgeving: om instellingen uit het .env-bestand te lezen.

##Functies
- Boeken toevoegen met titel, auteur en uitgavejaar
- Overzicht van alle boeken tonen
- Locaties toevoegen en tonen (boekID, depotnaam, plank)
- Export van de boekenlijst naar een CSV-bestand
- Database interactie via SQLite


##Hoe uitvoeren
1. Kloon de repository of download de code.

2.Creëer een virtuele omgeving.

python -m venv .venv
3. Externe bibliotheken installeren
pip install -r requirements.txt
4. Voer de code uit
python -m Examenopdrachtdecember2025


##Structuur van de database
De databases bestaan uit 2 tabellen:
    
CREATE TABLE "Boeken" (
	"id"	INTEGER,
	"Titel"	TEXT NOT NULL,
	"Auteur"	TEXT NOT NULL,
	"UitgaveJaar"	INTEGER NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
)    
    
 CREATE TABLE "Locatie" (
	"id"	INTEGER,
	"boekID"	INTEGER,
	"NaamDepot"	TEXT NOT NULL,
	"Plank"	INTEGER,
	FOREIGN KEY("boekID") REFERENCES "Boeken"("id"),
	PRIMARY KEY("id" AUTOINCREMENT)
)   
    
    
