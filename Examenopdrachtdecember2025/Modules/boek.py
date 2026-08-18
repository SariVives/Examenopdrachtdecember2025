# -*- coding: utf-8 -*-
"""
Repository voor boeken

"""
import csv
from Modules.domein import Boek

class BoekRepository:
    def __init__(self , dbconnectie):
        self.dbconnectie = dbconnectie
        
    def toevoegen(self, boek):
        cursor = self.dbconnectie.cursor()
        cursor.execute("INSERT INTO Boeken (Titel, Auteur, UitgaveJaar) VALUES (?,?,?)",(boek.titel, boek.auteur, boek.uitgave_jaar))
        self.dbconnectie.commit()
    
    def rapport_tonen(self):
        cursor = self.dbconnectie.cursor()
        cursor.execute("SELECT * FROM Boeken")
        boeken = []
        
        for rij in cursor.fetchall():
            boek = Boek(rij[0], rij[1], rij[2], rij[3])
            boeken.append(boek)
        return boeken
    
    def aanpassen(self, boek):
        cursor = self.dbconnectie.cursor()
        cursor.execute("UPDATE Boeken SET Titel = ?, Auteur = ?, UitgaveJaar = ? WHERE id = ?", (boek.titel, boek.auteur, boek.uitgave_jaar, boek.boek_id))
        self.dbconnectie.commit() 
        
    def verwijderen(self, boek_id):
        cursor = self.dbconnectie.cursor()
        # locatie van het boek verwijderen
        cursor.execute("DELETE FROM Locatie WHERE boekID = ?", (boek_id,))
        # Dan boek verwijderen
        cursor.execute("DELETE FROM Boeken WHERE id = ?",(boek_id,))
        self.dbconnectie.commit()
    
    def export_csv(self, bestand="boekenlijst.csv"):
        cursor = self.dbconnectie.cursor()
        cursor.execute("SELECT * FROM Boeken")
        data = cursor.fetchall()
        
        kolommen=[description[0] for description in cursor.description]
        
        with open(bestand,"w",newline="", encoding="utf-8") as bestand_csv:
            writer = csv.writer(bestand_csv)
            writer.writerow(kolommen)
            writer.writerows(data)
        
        print(f"export naar csv: {bestand}")
