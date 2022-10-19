# Создайте программу для игры с конфетами человек против человека.
# Правила: На столе лежит 150 конфет. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять
# первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота 'интеллектом'

from random import randint as ri

print('Правила: На столе лежит 150 конфет. Играют два игрока делая ход друг после друга.\n'
      'Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.\n'
      'Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять\n'
      'первому игроку, чтобы забрать все конфеты у своего конкурента?')
print()

count = 0
who = 0
player1 = False
player2 = False
bot = False
bot1 = 0
sweets = 150
takesweet = 0
swp1 = 0
swp2 = 0
run = True

bot1 = int(input('выберите с кем вы будете играть\n 1(человек) 2(компьютер): '))


who = (ri(1, 2))
if who == 1:
    player1 = True
    bot = False
    player2 = False
else:
    if bot1 == 2:
        bot = True
    else:
        player2 = True
        player1 = False


while run:
    run = False

    print(f'Cейчас в корзине {sweets} конфет')
    print()

    if player1:
        runp1 = True
        while runp1:
            print(f'Cейчас ход игрока 1\nВ корзине игрока {swp1} конфет')
            print()

            takesweet = int(input('Сколько конфет вы хотите взять?: '))
            if takesweet <= 28 and takesweet > 0 and sweets > 0 and takesweet<=sweets:
                for i in range(takesweet):
                    sweets -= 1

                for i in range(takesweet):
                    swp1 += 1
                runp1 = False
            
            else:
                print('Вы берете слишком много конфет, попробуйте снова!')
                print(f'Cейчас в корзине {sweets} конфет')
                print()
        player1 = False
        if bot1 == 2:
            bot = True
            player2 = False
        else:
            bot = False
            player2 = True
        print()

    elif player2:
        runp2 = True
        while runp2:
            print(f'Cейчас ход игрока 2\nв корзине игрока {swp2} конфет')
            print()
            takesweet = int(input('Сколько конфет вы хотите взять?: '))
            if takesweet <= 28 and takesweet > 0 and sweets > 0 and takesweet<=sweets:
                for i in range(takesweet):
                    sweets -= 1
                    swp2 += 1
                runp2 = False
            
            else:
                print('Вы берете слишком много конфет, попробуйте снова!')
                print(f'Cейчас в корзине {sweets} конфет')
                print()
        player2 = False
        if bot1 == 2:
            bot = True
            player1 = False
        else:
            bot = False
            player1 = True
        print()

    elif bot:
        print(f'Cейчас ход компьютера\nВ корзине игрока {swp1} конфет')
        print()

        if sweets > 80 and sweets % 2 == 0:
            print('Я возьму 28 конфет')
            sweets -= 28
            player1 = True
            bot = False
        elif sweets > 56 and sweets % 2 != 0:
            print('Я возьму 21 конфету')
            sweets -= 21
            player1 = True
            bot = False
        elif sweets < 28:
            print(f'Я возьму {sweets} конфет')
            sweets -= sweets
            player1 = True
            bot = False
        elif sweets > 28 and sweets <= 56:
            takesweet = 0
            for takesweet in range(28):
                if sweets - takesweet == 29:
                    print(f'Я возьму {takesweet} конфет')
                    sweets -= takesweet
            player1 = True
            bot = False    
        print()

    if sweets > 0:
        run = True
    else:
        if player1 and bot1 == 2:
            print('Победил компютер!!!')
            break
        elif player1 and bot1 == 1:
            print('Победил игрок 2!!!')
            break
        else:
            print('Победил игрок1!!!')