try:
    print(int(input('Введите число: ')))
    print('Вы ввели правильное число')
except ValueError:
    print('Неправильный формат ввода')
finally:
    print('Выход из программы')

