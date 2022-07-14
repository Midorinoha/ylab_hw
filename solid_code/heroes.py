from antagonistfinder import AntagonistFinder
from abc import ABC, abstractmethod

class SuperManAttack(ABC):
    @abstractmethod
    def incinerate_with_lasers(self):
        pass

class GeneralAttacks(ABC):
    @abstractmethod
    def fire_a_gun(self):
        pass

    @abstractmethod
    def roundhouse_kick(self):
        pass

class SuperHero(Heros, GeneralAttacks):
    
    def __init__(self, name, can_use_ultimate_attack=False):
        self.name = name
        self.can_use_ultimate_attack = can_use_ultimate_attack
        self.finder = AntagonistFinder()
        
    def find(self, place):
        self.finder.get_antagonist(place)

    def fire_a_gun(self):
         print('PIU PIU')

    def roundhouse_kick(self):
        print('Bump')

    def attack(self):
        self.fire_a_gun()

    def ultimate(self):
        pass

class Superman(SuperHero, SuperManAttack):

    def __init__(self, name = 'Clark Kent', can_use_ultimate_attack=True):
        self.name = name
        self.can_use_ultimate_attack = can_use_ultimate_attack
        self.finder = AntagonistFinder()

    def incinerate_with_lasers(self):
        print('Wzzzuuuup!')

    def attack(self):
        if not self.can_use_ultimate_attack:
            print('Kick')

    def ultimate(self):
        self.incinerate_with_lasers()
