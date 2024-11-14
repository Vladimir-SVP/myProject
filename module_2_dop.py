def input_number():
    n = 0
    while True:
        n = int(input('Введите число от 3 до 20: '))
        if n < 3 or n > 20:
            print('Вы ввели не правильное число! Попробуйте ещё раз.')
            continue
        else:
            break
    return(n)
entered_number = input_number()
result = []
for i in range(1,entered_number):
    for j in range(i+1,entered_number):
        if entered_number % (i+j) == 0:
            result.append(i)
            result.append(j)
print(f'Пароль для Вашего числа {entered_number}: ', *result, sep='')