def calculate_structure_sum(args):
    if args == []:
        return
    a = args[0]
    b = []
    if isinstance(a, int):
        b.append(a)
        return calculate_structure_sum(args[1:])
    if isinstance(a, list):
        for i in range(len(a)):
            b.append(a[i])
        return b, calculate_structure_sum(args[1:])
    return b
    
    


data_structure = [
    [1, 2, 3],
    [1, 2, 3],
    # {'a': 4, 'b': 5},
    # (6, {'cube': 7, 'drum': 8}),
    # "Hello",
    # ((), [{(2, 'Urban', ('Urban2', 35))}])
    ]
#print(**data_structure[1])

result = calculate_structure_sum(data_structure)

print(result)