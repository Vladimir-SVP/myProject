first = input('Введите первое целое число: ')
second = input('Введите второе целое число: ')
third = input('Введите третье целое число: ')
if not first.isdigit() or not second.isdigit() or not third.isdigit():
    print('Вы ввели не целое число!!! Попробуйте заново!')
else:
    if first == second and first == third:
        print('Одинаковых чисел: 3')
    elif first == second and first != third or second == third and second != first or first == third and first != second:
        print('Одинаковых чисел: 2')
    else:
        print('Одинаковых чисел: 0')