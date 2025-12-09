# -*- coding: utf-8 -*-
"""
Mijn examenopdracht voor Python December 2025
"""
from Modules.boek import Boeken
from Modules.locatie import Locatie
import sqlite3



def applicatie():
    dbconnectie = sqlite3.connect("Boekenlijst.db")
    
    boek = Boeken(dbconnectie)
    locatie = Locatie(dbconnectie)
    
    while True:
        print("Welkom in onze Boekenlijst, maak hieronder uw keuze:")
        print(" '1' = een boek toevoegen")
        print(" '2' = de volledige lijst tonen")
        print(" '3' = een locatie toevoegen")
        print(" '4' = alle locaties tonen")
        print(" '5' = een rapport afdrukken in CSV of Excel")
        print(" '0' = afsluiten van de applicatie")
        
        keuze = input("Kies uw volgende stap: ")
        
        if keuze == "1":
            titel = input("Titel: ")
            auteur = input("Auteur: ")
            jaar = input ("UitgaveJaar: ")
           
            boek.toevoegen(titel,auteur, jaar)
            print("Boek toegevoegd!")
        
        elif keuze == "2":
            for books in boek.rapport_tonen():
                print(books)
                
        elif keuze =="3":
            boekID = input ("BoekID:")
            depot = input("NaamDepot: ")
            plank = input("Plank: ")
            
            locatie.toevoegen(boekID, depot, plank)
            print("Locatie is toegevoegd!")
            
        elif keuze =="4":
            for location in locatie.rapport_tonen():
                print(location)
                
        elif keuze =="5":
            boek.export_csv()
            print("de boekenlijst is naar een csv bestand geëxporteerd.")
            
        
        elif keuze =="0":
            print("de applicatie wordt afgesloten")
            break
        
        else:
            print("ongeldige keuze")
            
    dbconnectie.close()
        
if __name__=="__main__":
    applicatie() 
    




        

        

