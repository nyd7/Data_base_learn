# Из алхимии импортируем модуль сортрировки по убыванию
# для фунцкии top_avg_salary_by_city, т.к. мы делаем сортировку
# по виртуальной колонке label('avg_salary'), а у Salary нет
# такого поля avg_salary, чтобы оно смогло проверисти по нему сортировку
from sqlalchemy import desc
# Модуль содержит дополнитеьные возможности по запросам
from sqlalchemy.sql import func

# Из db импортируем движок для связи с базой
from db import db_session
# Из файла модель - нашу модель (она уже содержит данные)
from model import Salary

# Все запросы оформляем в функции,
#  т.к. и будет много и так будет проще управялть
"""
top_salary - переменная куда вписать данные
Salary - наша модель
.query - запросить

.order_by() - порядок(сортировка)_по
desc - от большего к меньшему
asc - от меньшего к большему

.limit(num_rows) - кол-во выбираемых строк (размер выборки)
.all() - все - ??? Непонятно как распечатать!
Ответ: Мы получим объект, и по нему все равно надо проходить циклом.
Для этого необязательно писать .all() + вся база есть много памяти.

.filter - фльтр по()
.ilike() - неточное совпадение и плевать на регистр букв
.like() - неточное совпадение, но регистр влияет
Внутри like задаем Ф-строку f'%{domain}'
% - любые символы
{} - точные данные, в данном случае из конкретной переменной

.func() - как атрибут query .query(func())
.func() - дополнительные функции
.avg(Salary.salary)) - посчитать средее значение

.scalar() - вывести единственное число
Не итератор, объект, по которому мы делали цикл

.group_by(Salary.city) - группировать по (Модель, колонка)

.count() - посчитать кол-во строк

.label('avg_salary') - создание временной колонки в памяти

"""


# Топ зарплат в целом по базе
def top_salary(num_rows):
    top_salary = Salary.query.order_by(
        Salary.salary.desc()).limit(num_rows)
    # top_salary = Модель.Запросить.Порядок по(
    #   Моедль.Колонка salary.От большего к меньшему()
    #       ).Лимит(кол-во)
    # При этом top_salary будет некий объект... (просто не распечатать...)

    # Пройти по элементам top_salary, при этом s тоже будет
    # являться объектом класса
    for s in top_salary:
        # Печать перменной объекта s.salary обекта класса s
        print(f'З/п: {s.salary}')
    # print(top_salary.salary) ???


# Запрплты для конкретного города
def salary_by_city(city_name):
    top_salary = Salary.query.filter(
        Salary.city == city_name).order_by(Salary.salary.desc())
    # =Модель.Запрос.Фильтр(
    #   Модель.Колонка city = Заданный город
    #                       )
    #       .Сортировка по(
    #           Модель.Колонка salary. По убыванию()
    #                     )
    print(city_name)
    for s in top_salary:
        print(f'З/п: {s.salary}')


# Топ запрплат у кого почта заканчиваеся на @yandex.ru
def top_salary_by_domain(domain, num_rows):
    top_salary = Salary.query.filter(
        Salary.email.ilike(
            f'%{domain}')).order_by(
                Salary.salary).limit(num_rows)
    # =Модель.Запрос.Фильтр(
    #   Моедль.Колонка email.НЕЧЕТКОЕ совпадение
    #       (Ф-строка
    #           % -любые символы
    #                {что точно будет}))
    # .Порядок по (без desc) будет по возрастанию
    # .Лимит(num_rows)

    print(domain)
    for s in top_salary:
        print(f'З/п: {s.salary}')


# Средняя зараплата
def average_salary():
    # ОБРАЩАЕМСЯ НЕ К МОДЕЛИ,
    # а делаем запрос через движок соединения
    avg_salary = db_session.query(func.avg(Salary.salary)).scalar()
    # =Движок.Запрос(Доп_Функции.Средняя(Модель.Колонка salary)
    #   .Единственной значение
    print(f'Средняя зарплата {avg_salary:.2f}')
    # avg_salary:.2f - округлить до 2-х знаков после запятой


# Количество уинкальных городов
def count_distinct_cities():
    count_cities = db_session.query(Salary.city).group_by(Salary.city).count()
    # =Движок.Запрос(Модель.Колонка city)
    #   .груупировать по (Модель.Колонка city)
    #       .посчитать строки()

    print(f'Кол-во городов {count_cities}')


# Топ городов с самой большой средней зарплатой
def top_avg_salary_by_city(num_rows):
    top_salary = db_session.query(
        Salary.city,
        func.avg(Salary.salary).label('avg_salary')
    ).group_by(Salary.city).order_by(desc('avg_salary')).limit(num_rows)
    # =Движок.Запрос (
    #   Мы запрашивае 2 объекта:
    #       Модель.Колока city, (запятая!)
    """
    Возможно в этот момент мы создали много таблц Salary.city,
    потому как непонятно почему посчиталась средняя
    по каждому городу отдельно
    """
    #       Доп.фукции.Средняя(Модль, Колонка salary)
    #           .Создать ВРМЕННУЮ колокну (avg_salary)
    """В результате query вернет нам кортеж из 2-х позиций"""
    #                   )
    # .Группировать по(Модель.city)
    #   .Сортировать по(Убыванию(Колонка avg_salary)).Выдать кол-во позиций
    #

    for city, salary in top_salary:
        # Первое и второй значение кортежа в кортеже
        print(f'Город {city} - з/п {salary:.2f}')


if __name__ == '__main__':
    # top_salary(5)
    # salary_by_city('Адлер')
    # top_salary_by_domain('@yandex.ru', 5)
    # average_salary()
    # count_distinct_cities()
    top_avg_salary_by_city(5)
