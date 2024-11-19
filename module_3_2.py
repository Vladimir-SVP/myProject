def send_email(message, recipient, sender = "university.help@gmail.com"):
    domen = ['.com', '.ru', '.net']
    if '@' not in recipient or '@' not in sender and sender[-4:] not in domen[]:
        print('3')
    else:
        print('2')
send_email('Privet', 'acbfmail.net')