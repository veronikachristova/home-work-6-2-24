import json

class Krajiny_mesta:
    def __init__(self):
        self.data = {}

    def pridaj(self, krajina, mesto):
        self.data[krajina] = mesto

    def vymaz(self, krajina):
        if krajina in self.data:
            del self.data[krajina]
        else:
            print(f"{krajina} sa nenachádza v zozname.")

    def hladaj(self, krajina):
        if krajina in self.data:
            print(f"krajina: {krajina}, mesto: {self.data[krajina]}.")
        else:
            print(f"{krajina} nie je v zozname.")

    def uprav(self, krajina, nova_krajina, nove_mesto):
        if krajina in self.data:
            del self.data[krajina]
            self.data[nova_krajina] = nove_mesto
            print(
                f" krajina:{krajina} a jej mesto boli zmenene na: {nova_krajina} a mesto: {nove_mesto}")
        else:
            print(f"{krajina} not found.")

    def uloz(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.data, file)
        print("Zoznam ulozeny.")

    def loaduj(self, filename):
        try:
            with open(filename, 'r') as file:
                self.data = json.load(file)
            print("Zoznam je otvoreny.")
        except FileNotFoundError:
            print("Zoznam nenajdeny.")


krajiny_mesta = Krajiny_mesta()

krajiny_mesta.pridaj("USA", "Washington D.C.")
krajiny_mesta.pridaj("UK", "Londyn")
krajiny_mesta.pridaj("Francuzsko", "Pariz")

krajiny_mesta.uloz("Krajiny_mesta.json")

krajiny_mesta.vymaz("UK")
krajiny_mesta.uprav("USA", "New York", "Albany")

krajiny_mesta.hladaj("Francuzsko")


krajiny_mesta.loaduj("Krajiny_mesta.json")
