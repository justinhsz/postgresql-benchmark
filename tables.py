from default_db import db


def create_users():
    db.execute("""CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        first_name varchar(50) not null,
        last_name varchar(50) not null,
        birth_date date not null,
        register_date date not null,
        city varchar(100) not null,
        nationality varchar(100) not null
    );
    """)
