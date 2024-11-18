calls = 0
def count_calls():
    global calls
    calls += 1
def string_info(string):
    count_calls()
    result = (len(string), string.upper(), string.lower())
    return(result)
def is_contains(string, list_to_search):
    count_calls()
    if string.lower() in list(map(str.lower, list_to_search)):
        return True
    else:
        return False
print(string_info('MyProject'))
print(string_info('Instruсtion'))
print(string_info('Headphones'))
print(is_contains('Fish', ['fiSH', 'Fishing', 'ing']))
print(is_contains('mouse', ['muse', 'MOUses']))
print(calls)