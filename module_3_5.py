def get_multiplied_digits(number):
    str_number = str(number)
    
    first = 0
    first * get_multiplied_digits(int(str_number[1:]))
    return
result = get_multiplied_digits(40203)
print(result)