import csv
# Библиотека генерирующая случайные числа
import random
# Библиотека генерирующая случайные данные (как настоящие)
from faker import Faker

# Задаем что нужны данные на русском языке
# Объявляем fake объектом класса Faker
fake = Faker('ru_RU')


# Создаем функцию, которая создает список случайных данных
# создается одна случайная строка
def get_fake_row():
    return [fake.name(), fake.city_name(), fake.street_address(),
            fake.large_company(),
            fake.job(), fake.phone_number(), fake.free_email(),
            fake.date_of_birth(minimum_age=18, maximum_age=70),
            random.randint(20000, 200000)]


# Создаем функццию которая по циклу генерирует много фейковых строк
# и записывает все в csv файл
# через  num_rows задаем длину цикла, строк записей
def generate_data(num_rows=100):
    with open('salary.csv', 'w', encoding='utf-8') as f:
        # Заводим в writer значения файла salary.csv (f)
        # Заводить будем без задавания полей, с разделители ;
        writer = csv.writer(f, delimiter=';')
        # Кодна нам нужно просто пройти по циклу и не имеет значения
        # тот параметр, что мы перебираем - обычно обозначают "_"
        # т.е. мы эту переменную нигде больше не будем использовать
        # Если бы были задавали структуру колонок, то использовали бы
        # csv.DictWriter(f, fields, delimiter=';')
        # Проходим по диапазону num_rows
        for _ in range(num_rows):
            # В файл, обозначенный как writer
            # writerow - команда записать
            #  данные из функции get_fake_row
            writer.writerow(get_fake_row())


if __name__ == '__main__':
    generate_data()
