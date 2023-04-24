import datetime

import pandas as pd
from faker import Faker


MAX_ROWS_PER_BATCH = 10000


def create_users(num_of_records: int):
    fake: Faker = Faker('en_US')

    row_range = range(num_of_records)

    return pd.DataFrame(data={
        "first_name": [fake.first_name() for _ in row_range],
        "last_name": [fake.last_name() for _ in row_range],
        "birth_date": [fake.date_between(
            start_date=datetime.date(1990, 1, 1),
            end_date=datetime.datetime.now()
        ) for _ in row_range],
        "register_date": [fake.date_between(
            start_date=datetime.date(2014, 1, 1),
            end_date=datetime.datetime.now()
        ) for _ in row_range],
        "city": [fake.city() for _ in row_range],
        "nationality": [fake.country() for _ in row_range]
    })


if __name__ == '__main__':
    target_number_of_users = 1000000

    number_of_batches = int(target_number_of_users / MAX_ROWS_PER_BATCH)
    print("total iterate:", number_of_batches)

    for i in range(number_of_batches):
        print("iterate", i)

        pd.DataFrame(data=create_users(MAX_ROWS_PER_BATCH))\
            .to_csv(f"users_{target_number_of_users}.csv",
                    index=False,
                    header=False,
                    mode='a')
