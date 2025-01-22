def custom_write(file_name, strings):
    file = open(file_name, 'a+', encoding = 'utf-8')
    for i in strings:
        file.write((f'{i}\n'))
        line = file.readline()
        print(line)
    file.close
    return 

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]
result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)