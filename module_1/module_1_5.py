immutable_var = (15, 2, 'Hello', 2.3, True)
print('Immutable tuple:', immutable_var)

#immutable_var[4] = False

#Нельзя изменить кортеж, потому что он относиться к неизменяемым типам данных, так же как строки и числа.

mutable_list = [15, 2, 'Hello', 2.3, True]
mutable_list[4] = False
print('Mutable list:', mutable_list)