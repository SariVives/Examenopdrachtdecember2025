# -*- coding: utf-8 -*-
"""
Mijn examenopdracht voor Python December 2025
"""
class Boeken:
    def __init__(self , id, Titel, Auteur, UitgaveJaar):
        self.id = id
        self.Titel = Titel
        self.Auteur = Auteur
        self.UitgaveJaar = UitgaveJaar
        
class Locatie:
    def __init__(self, id, boekID, NaamDepot, Plank):
        self.id = id
        self.boekID = boekID
        self.NaamDepot = NaamDepot
        self.Plank = Plank
        
import sqlite3 
        
