# Вызвов сессии
from db import db_session
# Наша таблица
from models import User

first_user = User(name='Мария Сидрова', salary=1234, email='maria@example.com')

# Команда подготовки на добавление в облако конкретных данных (облачную базу)
# пользователя  first_user
db_session.add(first_user)
# Зафиксировать, записать все дбавления/изменения
db_session.commit()
