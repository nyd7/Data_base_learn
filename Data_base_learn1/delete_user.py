# И-ем вызов сессии
from db import db_session
# Наша таблица
from models import User

# my_user = Таблица.Запрос.Первый (по мнению базы данных)
my_user = User.query.first()

# Удалить пользователя my_user
db_session.delete(my_user)

# Зафиксировать, записать все дбавления/изменения
db_session.commit()
