from sqlalchemy import desc
from sqlalchemy.sql import func

from db import db_session
from model import Salary


def top_salary(num_rows):
    top_salary = Salary.query.order_by(Salary.salary.desc()).limit(num_rows)

    for s in top_salary:
        print(f'З/п: {s.salary}')


def salary_by_city(city_name):
    top_salary = Salary.query.filter(Salary.city == city_name).order_by(Salary.salary.desc())

    print(city_name)
    for s in top_salary:
        print(f'З/п: {s.salary}')


def top_salary_by_domain(domain, num_rows):
    top_salary = Salary.query.filter(Salary.email.ilike(f'%{domain}')).order_by(Salary.salary).limit(num_rows)

    print(domain)
    for s in top_salary:
        print(f'З/п: {s.salary}')


def average_salary():
    avg_salary = db_session.query(func.avg(Salary.salary)).scalar()
    print(f'Средняя зарплата {avg_salary:.2f}')


def count_distinct_cities():
    count_cities = db_session.query(Salary.city).group_by(Salary.city).count()
    print(f'Кол-во городов {count_cities}')


def top_avg_salary_by_city(num_rows):
    top_salary = db_session.query(
        Salary.city,
        func.avg(Salary.salary).label('avg_salary')
    ).group_by(Salary.city).order_by(desc('avg_salary')).limit(num_rows)

    for city, salary in top_salary:
        print(f'Город {city} - з/п {salary:.2f}')


if __name__ == '__main__':
    # top_salary(5)
    # salary_by_city('Дубна')
    # top_salary_by_domain('@yandex.ru', 5)
    # average_salary()
    # count_distinct_cities()
    top_avg_salary_by_city(5)
