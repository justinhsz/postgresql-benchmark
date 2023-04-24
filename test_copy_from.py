from timeit import default_timer

import tables
from default_db import db

if __name__ == '__main__':
    tables.create_users()

    for i in range(10):
        start = default_timer()

        db.bulk_insert(
            "users_1000000.csv", 'public', 'users',
            ("first_name", "last_name", "birth_date", "register_date", "city", "nationality")
        )

        print("ingest sequence", i, ", spent time:", default_timer() - start)
