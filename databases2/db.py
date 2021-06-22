# Т.к. Окружение запустил из общей папки Data_base_learn,
# поэтому пишет, что не нашел, на самом деле водной папке
# все прекрасно находит  (или нет??)
import config

# Разбор урл на логины, пароли, и пути
from sqlalchemy import create_engine

# Исходый модуль (Класс) базы данных
from sqlalchemy.ext.declarative import declarative_base

# Создатели сессии, в принципе, и ограниченную
from sqlalchemy.orm import sessionmaker, scoped_session

engine = create_engine(config.KEY_REMOTE_BASE)

"""
Создаем движок по созданию сессии в переменной db_session
scoped_session - ограниченная сессия
sessionmaker - создатель сессий
bind - связывать
Т.е. в ограниченной сессии создать сессию по связанному параметру engine,
где у нас храниться url удаленной базы данных.
"""
db_session = scoped_session(sessionmaker(bind=engine))

# Наша база будет по шаблону Деклоративной базы
Base = declarative_base()

# Способ связи для нашей базы брать из db_session, модуль query_..
Base.query = db_session.query_property()
