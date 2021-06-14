# И-ем вызов сессии
from db import db_session
# И-ем таблицу
from models import User

# my_user = Таблица.Запрос.Первый (по мнению базы данных)
my_user = User.query.first()

# Меняем параметр зарплаты my_user
my_user.salary = 300

# Зафиксировать, записать все дбавления/изменения
db_session.commit()
