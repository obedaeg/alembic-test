import os
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

target_metadata = None

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
    url = os.getenv('DB_CONNECTION')#config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    conf = config.get_section(config.config_ini_section)
    conf['sqlalchemy.url'] = os.getenv('DB_CONNECTION')
    print(conf)
    schema = conf['schema']
    print(schema)
    connectable = engine_from_config(
        conf,
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
        connect_args={'sslmode': 'verify-ca'}
    )

    with connectable.connect() as connection:
        # set search path on the connection, which ensures that
        # PostgreSQL will emit all CREATE / ALTER / DROP statements
        # in terms of this schema by default
        connection.execute("set search_path to %s" % schema)

        # make use of non-supported SQLAlchemy attribute to ensure
        # the dialect reflects tables in terms of the current tenant name
        connection.dialect.default_schema_name = schema

        context.configure(
            connection=connection, target_metadata=target_metadata,
            version_table_schema=schema
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
