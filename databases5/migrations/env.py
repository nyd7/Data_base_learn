"""
Данный файл env.py находится вложен в папку migrations,
и чтобы сюда можно было что-либо импортировать выше родительской папки,
без уточнений в виде точки и т.д.
мы в с систеный файл path, который содерить пути по которым программма ходит,
вставляем на нулевую (первую) позицию
 пупупуп = os.path.dirname(__file__) - путь к данному файлу
соесое = os.path.join(пупупуп, '..') - путь к файлу/.. - путь на папку выше
путище = os.path.realpath(соесое) - возвращает канонический путь, без "..""

(Если путь к объекту файла — Canonical,
он просто возвращает путь к текущему объекту файла.
Канонический путь всегда абсолютен и уникален,
функция удаляет «.» «..» с пути, если есть.)

sys.path.insert(0,путище)
sys.path.insert() - подключание каталога к списку путей,
в которых интерпритатор ищет модуль
0 - задаем, что это певоочерденой путь
путище - сам путь
"""
import os, sys
sys.path.insert(0, os.path.realpath(os.path.join(os.path.dirname(__file__), '..')))
"Теперь можем импортировать Base из Моделей"
from models import Base

from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context



# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = Base.metadata
"""
Вместо None поставили Base.metadata
Base.metadata - вся информация о наших моделях.
Теперь Алимбик будет просматривать удаленную базу, по пути,
что мы ему указали в alembic.ini - sqlalchemy.url
и информацию в Base.metadata, и в случае расхождения
создаст миграцию
"""


# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline():
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        # Когда мы изменели тип данных одной из колонок Алембик создал
        # пустую миграцию. Чтобы он отслеживал изменения типа -
        # дописываем код compare_type=True, здесь и чуть ниже
        compare_type=True,
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            # дописываем код compare_type=True, причина см. выше
            compare_type=True,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
