from sqlalchemy import Column, Integer, String, Date
# Т.к. Окружение запустил из общей папки Data_base_learn,
# поэтому пишет, что не нашел, на самом деле водной папке
# все прекрасно находит
from db import Base, engine


# Создали Модель Salary по образу Base (Salary подклас Base)
# Base при этом помнит все пути соединения и сам
# является частью системы Salary, Salary в него входит
class Salary(Base):
    # Название таблиц пишем во множествнном числе ...s
    __tablename__ = 'salaries'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    city = Column(String)
    address = Column(String)
    company = Column(String)
    job = Column(String)
    phone_number = Column(String)
    email = Column(String)
    date_of_birth = Column(Date)
    salary = Column(Integer)

    # Если будем тянуть не отдельные данные, а сам объект,
    # надо понимать что вернулось, а не адрес памяти
    def __repr__(self):
        return f"Salary {self.id}, {self.name}, {self.company}"


if __name__ == '__main__':
    # Созадание таблицы на облаке, базе данных.
    # Base в данном случае содержит унаследованую модель Salary
    # Создать все что есть в Base, связь по параметрам в engine
    Base.metadata.create_all(bind=engine)
