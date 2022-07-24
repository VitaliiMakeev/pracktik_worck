import re


def email_parse(email_address):
    """Функция парсинга email адреса. Возвращает словарь - имя: имя, домен: домен"""
    resalt = {}
    name = re.compile(r'\w+[@]\w+\.\w{2}')

    if name.findall(email_address):
        resalt['username'] = email_address.split('@')[0]
        resalt['domain'] = email_address.split('@')[1]
    else:
        msg = f'wrong email: {email_address}'
        raise ValueError(msg)
    return resalt

print(email_parse('someone@geekbrains.ru'))

