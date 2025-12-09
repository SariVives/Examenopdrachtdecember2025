# -*- coding: utf-8 -*-
"""
Mijn examenopdracht voor Python December 2025
"""
from Modules.boek import Boeken
from Modules.locatie import Locatie
import sqlite3

def applicatie():
    dbconnectie = sqlite3.connect("Boekenlijst.db")
    
    boek=Boeken(dbconnectie)
    locatie=Locatie(dbconnectie)
    
    While True:
        print("Welkom in onze Boekenlijst, maak hieronder uw keuze:")
        print(" '1' = een boek toevoegen")
        print(" '2' = de volledige lijst tonen")
        print(" '3' = een locatie toevoegen")
        print(" '4' = alle locaties tonen")
        print(" '5' = een rapport afdrukken in CSV of Excel")
        print(" '0' = afsluiten van de applicatie")
        
        

    




        

        

