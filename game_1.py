import random

print('Добро пожаловать в игру')
print('Попробуйте отгадать мое число от 1-100')
k = 10
a = random.randint(1, 100)
x = int(input('Введите число: '))
if x > a:
    k = 9
    print('Не попал)))')
    print('Забыл сказать,у тебя ограниченное количество попыток,всего их 10,ну теперь уже 9)')
    print(f'Я буду обозначать их так: "Количество попыток = {k}"')
    print('Чтож давай продолжим,теперь попробуй взять число поменьше')
    y = int(input('Введите число: '))
    if y > a:
        k = 8
        print('Уже теплее,попробуй ещё')
        print(f'Количество попыток = {k}')
        c = int(input('Введите число: '))
        if c != a:
            while c != a:
                if c > a:
                    if k != 1:
                        k -= 1
                        print('Чуток поменьше возьми')
                        print(f'Количество попыток = {k}')
                        c = int(input('Введите число: '))
                    else:
                        print('Количество попыток = 0')
                        print('Увы, но ты не смог угадать моё число(((')
                        print(f'Моё число было = {a}')
                        break
                if c < a:
                    if k != 1:
                        k -= 1
                        print('Чуток побольше возьми')
                        print(f'Количество попыток = {k}')
                        c = int(input('Введите число: '))
                    else:
                        print(f'Количество попыток = 0')
                        print('Увы, но ты не смог угадать моё число(((')
                        print(f'Моё число было = {a}')
                        break
            else:
                print('Поздравляю,вы отгадали')
    elif y == a:
        print('Поздравляю,вы отгадали моё число!')
    else:
        k = 8
        print('Полегче с оборотами уважаемый(ая),добавь немного')
        print(f'Количество попыток = {k}')
        g = int(input('Введите число: '))
        if g != a:
            while g != a:
                if g > a:
                    if k != 1:
                        k -= 1
                        print('Чуток поменьше возьми')
                        print(f'Количество попыток = {k}')
                        g = int(input('Введите число: '))
                    else:
                        print('Количество попыток = 0')
                        print('Увы, но ты не смог угадать моё число(((')
                        print(f'Моё число было = {a}')
                        break
                if g < a:
                    if k != 1:
                        k -= 1
                        print('Чуток побольше возьми')
                        print(f'Количество попыток = {k}')
                        g = int(input('Введите число: '))
                    else:
                        print(f'Количество попыток = 0')
                        print('Увы, но ты не смог угадать моё число(((')
                        print(f'Моё число было = {a}')
                        break
            else:
                print('Поздравляю,вы отгадали')
elif x == a:
    print('C 1 попытки? У вас определённо неплохая чуйка')
else:
    k = 9
    print('Не попал)))')
    print('Забыл сказать,у тебя ограниченное количество попыток,всего их 10,ну теперь уже 9)')
    print(f'Я буду обозначать их так: "Количество попыток = {k}"')
    print('Чтож давай продолжим,теперь попробуй взять число побольше')
    y = int(input('Введите число: '))
    if y < a:
        k = 8
        print('Уже теплее,попробуй ещё')
        print(f'Количество попыток = {k}')
        c = int(input('Введите число: '))
        if c != a:
            while c != a:
                if c > a:
                    if k != 1:
                        k -= 1
                        print('Чуток поменьше возьми')
                        print(f'Количество попыток = {k}')
                        c = int(input('Введите число: '))
                    else:
                        print('Количество попыток = 0')
                        print('Увы, но ты не смог угадать моё число(((')
                        print(f'Моё число было = {a}')
                        break
                if c < a:
                    if k != 1:
                        k -= 1
                        print('Чуток побольше возьми')
                        print(f'Количество попыток = {k}')
                        c = int(input('Введите число: '))
                    else:
                        print(f'Количество попыток = 0')
                        print('Увы, но ты не смог угадать моё число(((')
                        print(f'Моё число было = {a}')
                        break
            else:
                print('Поздравляю,вы отгадали')
    elif y == a:
        print('Поздравляю,вы отгадали моё число!')
    else:
        k = 8
        print('Полегче с оборотами уважаемый(ая),убавь немного')
        print(f'Количество попыток = {k}')
        g = int(input('Введите число: '))
        if g != a:
            while g != a:
                if g > a:
                    if k != 1:
                        k -= 1
                        print('Чуток поменьше возьми')
                        print(f'Количество попыток = {k}')
                        g = int(input('Введите число: '))
                    else:
                        print('Количество попыток = 0')
                        print('Увы, но ты не смог угадать моё число(((')
                        print(f'Моё число было = {a}')
                        break
                if g < a:
                    if k != 1:
                        k -= 1
                        print('Чуток побольше возьми')
                        print(f'Количество попыток = {k}')
                        g = int(input('Введите число: '))
                    else:
                        print(f'Количество попыток = 0')
                        print('Увы, но ты не смог угадать моё число(((')
                        print(f'Моё число было = {a}')
                        break
            else:
                print('Поздравляю,вы отгадали')