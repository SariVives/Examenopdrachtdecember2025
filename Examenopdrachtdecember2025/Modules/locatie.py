# -*- coding: utf-8 -*-
"""
aparte modules maken:Module Locatie
"""

class Locatie:
    def __init__(self, dbconnectie):
        self.dbconnectie = dbconnectie

    def toevoegen(self, boekID, NaamDepot, Plank):
        cursor = self.dbconnectie.cursor()
        cursor.execute("INSERT INTO Locatie (boekID, NaamDepot, Plank) VALUES (?,?,?)", (boekID, NaamDepot, Plank))
        self.dbconnectie.commit()
        
    def rapport_tonen(self):
        cursor = self.dbconnectie.cursor()
        cursor.execute("SELECT * FROM Locatie")
        return cursor.fetchall()