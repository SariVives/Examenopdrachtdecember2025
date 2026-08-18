# -*- coding: utf-8 -*-
"""
Domeinklassen van de applicatie
"""

class Boek:
    def __init__(self, boek_id, titel, auteur, uitgave_jaar):
        self.boek_id = boek_id
        self.titel = titel
        self.auteur = auteur
        self.uitgave_jaar = uitgave_jaar

    def __str__(self):
        return f"{self.boek_id} - {self.titel} - {self.auteur} - {self.uitgave_jaar}"


class Locatie:
    def __init__(self, boek_id, naam_depot, plank):
        self.boek_id = boek_id
        self.naam_depot = naam_depot
        self.plank = plank

    def __str__(self):
        return f"BoekID: {self.boek_id} - Depot: {self.naam_depot} - Plank: {self.plank}"