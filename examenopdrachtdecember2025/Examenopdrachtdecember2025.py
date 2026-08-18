# -*- coding: utf-8 -*-
"""
Mijn examenopdracht voor Python December 2025 herexamenopdracht augustus 2026
"""

import sqlite3
import config
from Modules.domein import Boek, Locatie
from Modules.boek import BoekRepository
from Modules.locatie import LocatieRepository



def applicatie():
    dbconnectie = sqlite3.connect(config.DB_PATH)
    
    boek_repository = BoekRepository(dbconnectie)
    locatie_repository = LocatieRepository(dbconnectie)
    
    while True:
        print("Welkom in onze Boekenlijst, maak hieronder uw keuze:")
        print(" '1' = een boek toevoegen")
        print(" '2' = de volledige lijst tonen")
        print(" '3' = een boek aanpassen")
        print(" '4' = een boek verwijderen")
        print(" '5' = een locatie toevoegen")
        print(" '6' = alle locaties tonen")
        print(" '7' = een locatie aanpassen")
        print(" '8' = een locatie verwijderen")
        print(" '9' = een rapport afdrukken in CSV")
        print(" '0' = afsluiten van de applicatie")
        
        keuze = input("Kies uw volgende stap: ")
        
        if keuze == "1":
            titel = input("Titel: ")
            auteur = input("Auteur: ")
            uitgave_jaar = int(input ("UitgaveJaar: "))
           
            boek = Boek(None, titel, auteur, uitgave_jaar)
           
            boek_repository.toevoegen(boek)
            print("Boek toegevoegd!")
        
        elif keuze == "2":
            boeken = boek_repository.rapport_tonen()
            for boek in boeken:
                print(boek)
        
        elif keuze == "3":
            boek_id = int(input("BoekID van het boek dat je wilt aanpassen: "))
            titel = input("Nieuwe titel: ")
            auteur = input("Nieuwe auteur: ")
            uitgave_jaar = int(input("Nieuw uitgavejaar: "))
            
            boek = Boek(boek_id, titel, auteur, uitgave_jaar)
            boek_repository.aanpassen(boek)
            print("Boek aangepast!")
            
        elif keuze == "4":
            boek_id = int(input("BoekID van het boek dat je wilt verwijderen: "))
            boek_repository.verwijderen(boek_id)
            print("Boek verwijderd!")
        
                
        elif keuze =="5":
            boek_id = int(input ("BoekID:"))
            naam_depot = input("NaamDepot: ")
            plank = int(input("Plank: "))
            
            locatie = Locatie(boek_id, naam_depot, plank)
            
            locatie_repository.toevoegen(locatie)
            print("Locatie is toegevoegd!")
            
        elif keuze =="6":
            locaties = locatie_repository.rapport_tonen()
            
            for locatie in locaties:
                print(locatie)
                
        elif keuze == "7":
            boek_id = int(input("BoekID van het boek waarvan je de locatie wilt aanpassen: "))
            naam_depot = input("Nieuwe naam depot: ")
            plank = int(input("Nieuwe plank: "))
            
            locatie_repository.aanpassen(locatie)
            print("Locatie aangepast!")
            
        elif keuze == "8":
            boek_id = int(input("BoekID van de locatie die je wilt verwijderen: "))
            
            locatie_repository.verwijderen(boek_id)
            print("Locatie verwijderd!")
                
        elif keuze =="9":
            boek_repository.export_csv()
            print("de boekenlijst is naar een csv bestand geëxporteerd.")
            
        
        elif keuze =="0":
            print("de applicatie wordt afgesloten")
            break
        
        else:
            print("ongeldige keuze")
            
    dbconnectie.close()
        
if __name__=="__main__":
    applicatie() 
    




        

        

