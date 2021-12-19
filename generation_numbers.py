import psycopg2
import random

connection = psycopg2.connect(
    database="postgres",
    user="postgres",
    password="15062001",
    host="127.0.0.1",
    port="5432"
)
connection.autocommit = True


def random_number():
    num = '+7'
    for _ in range(10):
        num += str(random.randint(0, 9))
    return num


select_porters_SQL = "SELECT porter_id FROM porters"
select_customers_SQL = "SELECT customer_id FROM customers"

with connection.cursor() as cursor:
    cursor.execute(select_porters_SQL)
    rows_porters_raw = cursor.fetchall()

    cursor.execute(select_customers_SQL)
    rows_customers_raw = cursor.fetchall()

porters = list(map(lambda s: s[0], rows_porters_raw))
customers = list(map(lambda s: s[0], rows_customers_raw))


insertSQL = "INSERT INTO numbers (number_number, number_porter_id, number_customer_id) VALUES (%s, %s, %s)"
length_porters = len(porters)
length_customers = len(customers)

with connection.cursor() as cursor:
    for i in range(length_porters):
        if i % 19 == 0:
            cursor.execute(insertSQL, (random_number(), porters[i], None,))
        cursor.execute(insertSQL,  (random_number(), porters[i], None,))
    for j in range(length_customers):
        if i % 11 == 0:
            cursor.execute(insertSQL, (random_number(), None, customers[j],))
        cursor.execute(insertSQL, (random_number(), None, customers[j],))

connection.close()
