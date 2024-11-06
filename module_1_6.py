my_dict = {'Коля': 1993,
           'Иван': 2001,
           'Марина': 1987,
           'Ира': 2005}
print('Dict:', my_dict)
print('Existing value:', my_dict['Ира'])
print('Not existing value:', my_dict.get('Даша'))
my_dict.update({'Миша': 1984,
                'Люба': 1998})
name = my_dict.pop('Марина')
print('Deleted value:', name)
print('Modified dictionary:', my_dict)

my_set = {1, 3, 6, 'Вася', 4.6, 3, 1, 'Вася', 'Петя'}
print('Set:', my_set)
my_new_set = {7, (7,8)}
my_set.update(my_new_set)
my_set.discard('Петя')
print('Modified set:', my_set)