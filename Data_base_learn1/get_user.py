# Импортируем нашу таблицу
from models import User

# Почему при запрос данных мы не созадем новую сессию???

# my_user = Таблица.Запрос.Первого
#  User. - именно имя класса
my_user = User.query.first()
# print(my_user) - если запросить весь объект целиком,
# то мы получим сообщение, где этот объект находится в памяти
# Но нас выручает встроенный __repr__, который вывадст name & email


print(f"""Имя: {my_user.name}
Зарплата: {my_user.salary}
Email: {my_user.email}""")
