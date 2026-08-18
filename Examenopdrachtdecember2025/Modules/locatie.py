# -*- coding: utf-8 -*-
"""
Repository voor locaties
"""

from Modules.domein import Locatie

class LocatieRepository:
    def __init__(self, dbconnectie):
        self.dbconnectie = dbconnectie

    def toevoegen(self, locatie):
        cursor = self.dbconnectie.cursor()
        cursor.execute("INSERT INTO Locatie (boekID, NaamDepot, Plank) VALUES (?,?,?)", (locatie.boek_id, locatie.naam_depot, locatie.plank))
        self.dbconnectie.commit()
        
    def rapport_tonen(self):
        cursor = self.dbconnectie.cursor()
        cursor.execute("SELECT * FROM Locatie")
        locaties = []
        
        for rij in cursor.fetchall():
            locatie = Locatie(rij[1], rij[2], rij[3])
            locaties.append(locatie)
        return locaties
    
    def aanpassen(self, locatie):
        cursor = self.dbconnectie.cursor()
        cursor.execute("UPDATE Locatie SET NaamDepot = ?, Plank = ? WHERE boekID = ?",(locatie.naam_depot, locatie.plank, locatie.boek_id))
        self.dbconnectie.commit()
        
    def verwijderen(self, boek_id):
        cursor = self.dbconnectie.cursor()
        cursor.execute("DELETE FROM Locatie WHERE boekID = ?",(boek_id,))
        self.dbconnectie.commit()
        