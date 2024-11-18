calls = 0
def count_calls():
    global calls
    calls += 1
def string_info(string):
    count_calls()
    result = (len(string), string.upper(), string.lower())
    return(result)
def is_contains(string, list_to_search):
    
print(string_info('Capybara'))
print(calls)