def send_email(message, recipient, sender = "university.help@gmail.com"):
    domen = ('.com', '.ru', '.net')
    if '@' not in recipient or '@' not in sender or not recipient.endswith(domen) or not sender.endswith(domen):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}.')
    elif sender == recipient:
        print('Нельзя отправить письмо самому себе.')
    elif sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')
send_email('Privet', 'acbf@mail.net')