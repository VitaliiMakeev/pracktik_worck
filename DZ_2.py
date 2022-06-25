import requests
import requests.utils
import datetime


# Домашние задания к 4 уроку.
# Задание 2
# Задание 3
# В консоли запускать через utils.py


def currensy_rates(code):
    """Эта функция принимает 1 аргумент - code -> str (код валюты)"""
    """Возвращает курс валюты -> Float и дату запроса"""
    code_val = code.upper()
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    encoding = requests.utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encoding)
    f_strok = content.split('/')
    data = f_strok[0].split()
    result = None
    for _ in data:
        if 'Date' in _:
            day = int(_[6:8])
            month = int(_[9:11])
            year = int(_[12:16])
            data_in = datetime.date(day=day, month=month, year=year)
    for i in f_strok:
        n = f_strok.index(i)
        if code_val in i:
            curs = f_strok[n + 3].split('>')[-1]
            curs_in = curs.replace('<', '')
            curs_flo = curs_in.replace(',', '.')
            curs_float = float(curs_flo)
            result = f'{curs_float}, {data_in}'
    return result




if __name__ == '__main__':
    print(currensy_rates('USD'))
    print(currensy_rates('EuR'))
    print(currensy_rates('GBP2'))