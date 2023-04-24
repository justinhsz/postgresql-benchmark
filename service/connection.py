from typing import Tuple, cast

import pandas as pd
from psycopg import connection, cursor
from sqlalchemy import create_engine


class Postgres:
    def __init__(self, user, password, database='postgres', host='127.0.0.1', port='5432'):
        self._engine = create_engine(f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}")

    def query(self, sql_statement: str):
        conn = cast(connection, self._engine.raw_connection())
        try:
            cur: cursor = conn.cursor()
            cur.execute(sql_statement)
            result = cur.fetchall()
        finally:
            conn.close()

        return result

    def execute(self, sql_statement: str):
        """
        Perform DML SQL Statement.
        :param sql_statement:
        """
        conn = cast(connection, self._engine.raw_connection())
        try:
            cur = conn.cursor()
            cur.execute(sql_statement)
            conn.commit()

            print(cur.fetchone())
        except Exception as err:
            print(err)
        finally:
            conn.close()

    def insert_into(self, data: pd.DataFrame, schema: str, table: str):
        with self._engine.connect() as conn:
            data.to_sql(table, conn, schema=schema, method='multi', if_exists='append', index=False, chunksize=1000)

    def bulk_insert(self, file: str, schema: str, table: str, columns: Tuple):
        """
        Perform `COPY FROM STDIN` to insert large amount of data
        :param file:
        :param schema:
        :param table:
        :param columns:
        """
        conn = cast(connection, self._engine.raw_connection())
        try:
            cur = conn.cursor()
            cur.execute(f"set schema '{schema}';")
            f = open(file, 'r')
            cur.copy_from(f, table=table, sep=",", columns=columns)
        except Exception as err:
            print(err)
        finally:
            conn.commit()
            conn.close()
