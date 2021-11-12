# coding: utf-8
# license: GPLv3
from abc import ABC, abstractmethod

class Character(ABC):
    _health = None
    _attack = None
    _heal = None

class Attacker(Character):

    def attack(self, target):
        target._health -= self._attack

    def is_alive(self):
        return self._health > 0

class Peaceful(Character):

    def heal(self):
        target._health += self.heal
