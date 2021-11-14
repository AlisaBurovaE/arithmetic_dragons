# coding: utf-8
# license: GPLv3
from enemies import *
from hero import *

def annoying_input_int(message =''):
    answer = None
    while answer == None:
        try:
            answer = int(input(message))
        except ValueError:
            print('Вы ввели недопустимые символы')
    return answer


def game_tournament(hero, dragon_list, troll_list):
    for dragon in dragon_list:
        print('Вышел', dragon._color, 'дракон!')
        while dragon.is_alive() and hero.is_alive():
            print('Вопрос:', dragon.question())
            answer = annoying_input_int('Ответ:')

            if dragon.check_answer(answer):
                hero.attack(dragon)
                print('Верно! \n** дракон кричит от боли **')
            else:
                dragon.attack(hero)
                print('Ошибка! \n** вам нанесён удар... **')
        if dragon.is_alive():
            break
        print('Дракон', dragon._color, 'повержен!\n')

    if hero.is_alive():
        print('Поздравляем! Вы победили!')
        print('Ваш накопленный опыт:', hero._experience)
        if hero._health < 50:
            fairy = Fairy(self)
            fairy.heal(hero)
        for troll in troll_list:
            print('Вышел', troll._type, 'тролль!')
            while troll.is_alive() and hero.is_alive():
                print('Вопрос:', troll.question())
                answer = annoying_input_int('Ответ:')
                if troll.check_answer(answer):
                    hero.attack(troll)
                    print('Верно! \n** Вы ранили тролля **')
                else:
                    troll.attack(hero)
                    print('Ошибка! \n** вам нанесён удар... **')
            if troll.is_alive():
                break
            print(troll._type, 'тролль повержен!\n')

        if hero.is_alive():
            print('Поздравляем! Вы победили!')
            print('Ваш накопленный опыт:', hero._experience)
        else:
            print('К сожалению, Вы проиграли')

    else:
        print('К сожалению, Вы проиграли...')
    

def start_game():

    try:
        print('Добро пожаловать в арифметико-ролевую игру с драконами!')
        print('Представьтесь, пожалуйста: ', end = '')
        hero = Hero(input())

        dragon_number = 3
        dragon_list = generate_dragon_list(dragon_number)
        assert(len(dragon_list) == 3)
        troll_number = 2
        troll_list = generate_troll_list(troll_number)
        assert(len(troll_list) == 2)
        print('У Вас на пути', dragon_number, 'драконов!')
        game_tournament(hero, dragon_list, troll_list)

    except EOFError:
        print('Поток ввода закончился. Извините, принимать ответы более невозможно.')
