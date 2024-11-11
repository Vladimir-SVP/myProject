my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
count_list = len(my_list)
i = 0
print('Начало цикла:')
while i < count_list:
    if int(my_list[i]) > 0:
        print(my_list[i])
        i += 1
    elif int(my_list[i] == 0):
        i += 1
        continue
    else:
        break
print('***Конец цикла!***')