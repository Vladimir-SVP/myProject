def input_number():
    n = int(input('Введите число от 3 до 20: '))
    while True:
        if n < 3 or n > 20:
            print('Вы ввели не правильное число! Попробуйте ещё раз.')
            continue
        else:
            break 
    return(n)
a = input_number()

print(a)
# n = list(range(3,21))
# print(n)