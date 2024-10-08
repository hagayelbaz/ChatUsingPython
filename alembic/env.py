from logging.config import fileConfig
from flask import current_app
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
fileConfig(config.config_file_name)

# access the current application context and set up the database URL
from app import create_app, db  # Import your app and db here

app = create_app()  # Create an app instance

with app.app_context():
    # Set the database URL for Alembic from the Flask app's config
    config.set_main_option('sqlalchemy.url', app.config.get('SQLALCHEMY_DATABASE_URI'))

# add your model's MetaData object here
target_metadata = db.metadata

def run_migrations_offline():
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()  # <--- Use run_migrations()

def run_migrations_online():
    """Run migrations in 'online' mode."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )

        with context.begin_transaction():
            context.run_migrations()  # <--- Use run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
