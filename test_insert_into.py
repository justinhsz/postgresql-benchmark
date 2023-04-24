from timeit import default_timer

import pandas as pd

import tables
from default_db import db

if __name__ == '__main__':
    tables.create_users()

    # "users_1000000.csv"
    data = pd.read_csv("users_1000000.csv", index_col=None, header=None, names=[
        "first_name", "last_name", "birth_date", "register_date", "city", "nationality"
    ], parse_dates=["birth_date", "register_date"], low_memory=True)

    for i in range(10):
        start = default_timer()
        db.insert_into(data, 'public', 'users')
        print("ingest sequence", i, ", spent time:", default_timer() - start)
