from abc import ABC, abstractmethod
from typing import List

class Place(ABC):
    name: str
    planet: List[float]

    @abstractmethod
    def get_monster(self):
        pass

class Kostroma(Place):
    name = 'Kostroma'
    planet = [5.696, 9.252]

    def get_monster(self):
        print('Orcs hid in the forest')

class Tokyo(Place):
    name = 'Tokyo'
    planet = [5.696, 9.252]

    def get_monster(self):
        print('Godzilla stands near a skyscraper')
