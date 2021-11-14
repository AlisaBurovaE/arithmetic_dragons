# coding: utf-8
# license: GPLv3
from gameunit import *
from random import randint, choice

class Enemy(Attacker):
    pass


def generate_random_enemy():
    RandomEnemyType = choice(enemy_types)
    enemy = RandomEnemyType()
    return enemy


def generate_dragon_list(enemy_number):
    enemy_list = [generate_random_enemy() for i in range(enemy_number)]
    return enemy_list

def generate_dragon_list(enemy_number):
    enemy_list = [generate_random_enemy() for i in range(enemy_number)]
    return enemy_list


def generate_troll_list(enemy_number):
    enemy_list = [generate_random_enemy() for i in range(enemy_number)]
    return enemy_list



class Dragon(Enemy):
    def set_answer(self, answer):
        self.__answer = answer

    def check_answer(self, answer):
        return answer == self.__answer


class GreenDragon(Dragon):
    def __init__(self):
        self._health = 200
        self._attack = 10
        self._color = 'зелёный'

    def question(self):
        x = randint(1,100)
        y = randint(1,100)
        self.__quest = str(x) + '+' + str(y)
        self.set_answer(x + y)
        return self.__quest


class RedDragon(Dragon):
    def __init__(self):
        self._health = 200
        self._attack = 10
        self._color = 'красный'
    def question(self):
        x = randint(1,100)
        y = randint(1,100)
        self.__quest = str(x) + '-' + str(y)
        self.set_answer(x - y)
        return self.__quest

class BlackDragon(Dragon):
    def __init___(self):
        self._health = 200
        self._attack = 10
        self._color = 'чёрный'
    def question(self):
        x = randint(1,100)
        y = randint(1,100)
        self.__quest = str(x) + '*' + str(y)
        self.set_answer(x * y)
        return self.__quest

class Troll(Enemy):
    def set_answer(self, answer):
        self.__answer = answer

    def check_answer(self, answer):
        return answer == self.__answer

class MountainTroll(Troll):
    def __init__(self):
        self._health = 150
        self._attack = 15
        self._type = 'горный'
    def question(self):
        x = randint(1,100)
        self.__quest = 'Является ли' + str(x) + 'простым числом?'
        def func_for_mountaintroll(i):
            k = 0
            for j in range(2, i // 2+1):
                if (i % j == 0):
                    k += 1
            if (k <= 0):
                return True
            else:
                return False
        if func_for_mountaintroll(x):
            self.set_answer('Да')
        else:
            self.set_answer('Нет')
        return self.__quest

class CaveTroll(Troll):
    def __init__(self):
        self._health = 150
        self._attack = 15
        self._type = 'пещерный'
    def question(self):
        x = randint(1,100)
        self.__quest = 'Разложите' + str(x) + 'на множители'
        def func_for_cavetroll(i):
            lst = list()
            d = 2
            while d * d <= i:
                if i % d == 0:
                    lst.append(d)
                    i //= d
                else:
                    d += 1
            if i > 1:
                lst.append(i)
            return lst
        self.set_answer(",".join(lst))
        return self.__quest
        

    


#FIXME: описаны классы RedDragon и BlackDragon, а также Mountain Troll и CaveTroll
# красный дракон учит вычитанию, а чёрный -- умножению, горный тролль - проверке числа на простоту, пещерный - разложению на множители

