# -*- coding: utf-8 -*-
"""
aparte modules maken:Module Boek

"""
import csv

class Boeken:
    def __init__(self , dbconnectie):
        self.dbconnectie = dbconnectie
        
    def toevoegen(self, Titel, Auteur, UitgaveJaar):
        cursor = self.dbconnectie.cursor()
        cursor.execute("INSERT INTO Boeken (Titel, Auteur, UitgaveJaar) VALUES (?,?,?)",(Titel, Auteur, UitgaveJaar))
        self.dbconnectie.commit()
    
    def rapport_tonen(self):
        cursor = self.dbconnectie.cursor()
        cursor.execute("SELECT * FROM Boeken")
        return cursor.fetchall()
    
    def export_csv(self,bestand="boekenlijst.csv"):
        cursor = self.dbconnectie.cursor()
        cursor.execute("SELECT * FROM Boeken")
        data = cursor.fetchall()
        
        kolommen=[description[0] for description in cursor.description]
        
        with open(bestand,"w",newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(kolommen)
            writer.writerows(data)
        
        print(f"export naar csv: {bestand}")
