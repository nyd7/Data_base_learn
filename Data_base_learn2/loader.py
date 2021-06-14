# Загрзка данных из файла csv в базу данных
import csv
import time

from db import db_session
from model import Salary


# Читаем наш файл csv
# 1. Открываем файл
# 2. Создаем имена полей, и пишем их в том порядке,
# как они заложены по смыслу в csv файле
# В данном случае заголовки полей становяться ключами словаря,
# где значение по ключу - это данные в текущей просматриваемой строке.
# 3. Записываем все данные в переменную reader
# 4. Проходим по каждой строке reader-а
# 5. Запускаем функцию записи в базу данных
def read_csv(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        fields = ['name', 'city_name', 'street_address',
                  'large_company', 'job', 'phone_number',
                  'free_email', 'date_of_birth', 'salary']
        reader = csv.DictReader(f, fields, delimiter=';')
        for row in reader:
            save_salary_data(row)


# Функция записи в базу данных по строчно
# Создаем объект класса salary, как объект класса Salary, с заполненными
# всеми необходимыми полями
# У нас уже есть модель Salary с колонками name, city, address и т.д.
# Передаем им значения, как значение по ключу словаря row,
# а row это (словарь) и текущая просматриваемая строка в read_csv
def save_salary_data(row):
    salary = Salary(name=row['name'],
                    city=row['city_name'],
                    address=row['street_address'],
                    company=row['large_company'],
                    job=row['job'],
                    phone_number=row['phone_number'],
                    email=row['free_email'],
                    date_of_birth=row['date_of_birth'],
                    salary=row['salary'])

    # Добавляем объект salary в базу (адрес базы в db_session) как в Git-е
    # Движок по созданию сессии.Добавить.Объект(salary)
    db_session.add(salary)
    # Фиксируем все как в Git-е
    # Движок по созданию сессии.Фиксировать все
    db_session.commit()


# СПОСОБ 2. Передача пакетом. Быстрее.
# ВАЖНО! Чтобы наши названия полей (ключей) совпадали с
# названиями переменных в Модели класса Salary,
# он же колоноки в базе данных
# filename = 'salary.csv'
def read_csv2(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        fields = ['name', 'city', 'address',
                  'company', 'job', 'phone_number',
                  'email', 'date_of_birth', 'salary']
        reader = csv.DictReader(f, fields, delimiter=';')
        # Создаем список словарей, куда запишем все сгенерированные данные
        salary_data = []
        for row in reader:
            salary_data.append(row)
        # Добавляем в базу весь словарь salary_data
        #  через функцию save_salary_data2
        save_salary_data2(salary_data)


# Функция записи в базу данных Словарем
#  на вход получаем salary_data
def save_salary_data2(data):
    db_session.bulk_insert_mappings(Salary, data)
    # bulk - масса
    # _insert - вставить
    # _mappings - сопоставить
    # (Salary - Наша медель, которую хотим заполнить
    # data) - данные из словаря salary_data
    # далее sqlalchemy сама распихает данные в базу данных

    db_session.commit()


if __name__ == '__main__':
    # start = time.time()
    # read_csv('salary.csv')
    # print(f'Загрузка1 заняла {time.time() - start} сек.')

    # Время сильно зависит, как далеко находится наше облако с базой данных

    start = time.time()
    read_csv2('salary.csv')
    print(f'Загрузка2 заняла {time.time() - start} сек.')
