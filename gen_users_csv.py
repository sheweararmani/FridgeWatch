import csv
import random

file_name = "users.csv"
num_of_unique_users = 10
total_rows = 100
product_count = 140


def _gen_date():
    """Generate a date."""
    yyyy = "2019"
    dd = str(random.randint(10, 28))
    mm = "0" + str(random.randint(1, 9))
    return yyyy + "-" + mm + "-" + dd


def gen_file():
    """Generates a users.csv file with random data."""

    data = []
    for i in range(100):
        user_id = random.randint(0, num_of_unique_users)
        product = random.randint(1, product_count)
        date = _gen_date()
        data.append([user_id, product, date])

    with open("users.csv", "w", newline="") as f:
        writer = csv.writer(f, delimiter=',')
        for item in data:
            writer.writerow(item)
