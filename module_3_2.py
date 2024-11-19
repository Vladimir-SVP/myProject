def send_email(message, recipient, sender = "university.help@gmail.com"):
    if '@' and '.net' not in recipient and '@' and '.net' not in sender:
        print('3')
    else:
        print('2')
send_email('Privet', 'acbf@mail.net')