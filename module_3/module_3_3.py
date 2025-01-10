def print_params(a = 1990, b = 'String', c = True):
    print(a, b, c)
print_params(3, 56, 'Str')
# print_params(3, 56, 'Str', 45, True)   Не будет работать, т.к. функция принимает 3 параметра.
print_params()
print_params(b = 25) 
print_params(c = [1,2,3])

values_list = [[21, 31, 41], 5.7, False]
values_dict = {'a': 'Str', 'b': 56, 'c': True}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [True, ['a', 3, False]]
print_params(*values_list_2, 42)