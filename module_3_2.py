def send_email(message, recipient, sender = "university.help@gmail.com"):
    domen = ['.com', '.ru', '.net']
    for i in range(0, len(domen)):
        if ('@' not in recipient or '@' not in sender) and (domen[i] not in sender[-4:] or domen[i] not in recipient[-4:]):
            print(sender[-4:])            
        else:
            print('2')
            print(type(domen[i]))
send_email('Privet', 'acbf@mail.net')